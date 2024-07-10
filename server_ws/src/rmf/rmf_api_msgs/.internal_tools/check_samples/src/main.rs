#![feature(path_file_prefix)]

use argparse::{ArgumentParser, Store};
use jsonschema::CompilationOptions;
use serde_json::Value;
use configure_validator;
use std::collections::HashMap;

fn generate_schema_file_map(schema_directory: &str) -> HashMap<String, String> {
    let mut map = HashMap::<String, String>::new();
    for entry in std::fs::read_dir(&schema_directory).unwrap() {
        let file = entry.unwrap();
        map.insert(file.path().file_prefix().unwrap().to_str().unwrap().to_string(), file.path().to_str().unwrap().to_string());
        let idx = file.path().file_prefix().unwrap().to_str().unwrap().to_string();
        let ele = file.path().to_str().unwrap().to_string();
        println!("file: {}  -> {}", idx, ele);
    }   
    return map;
}

fn check_samples(schema_directory: &str, sample_directory: &str, options: CompilationOptions) -> bool {

    let schema_file_map = generate_schema_file_map(&schema_directory);
    println!("---------------------------------------\n");
    let mut error_found = false;
    for subdirectory_entry in std::fs::read_dir(&sample_directory).unwrap() {
        let subdirectory = subdirectory_entry.unwrap().path();
        if subdirectory.is_dir() {
            let schema_type = subdirectory.file_prefix();
            let schema_path = schema_file_map.get(&schema_type.unwrap().to_str().unwrap().to_string()).unwrap();
            let schema_str = std::fs::read_to_string(&schema_path).unwrap();
            let schema: Value = serde_json::from_str(&schema_str).unwrap();
            let validator_result = options.compile(&schema);
            match validator_result {
                Ok(validator) => {
                    for entry in std::fs::read_dir(&subdirectory).unwrap() {
                        let sample_file = entry.unwrap();
                        let sample_str = std::fs::read_to_string(&sample_file.path()).unwrap();
                        println!("##############################\n sample file: {} with {} ->\n {}",
                                 sample_file.path().to_str().unwrap(), schema_path, sample_str);

                        let sample: Value = serde_json::from_str(&sample_str).unwrap();
                        let validation = validator.validate(&sample);
                        if let Err(errors) = validation {
                            println!("Errors in {}:", sample_file.path().to_str().unwrap());
                            for error in errors {
                                println!(" -- {}", error);
                            }
                            error_found = true;
                        }
                    }
                },
                Err(err) => {
                    println!("Error in {}: {}", schema_path, err.to_string());
                    error_found = true;
                }
            }
        }
    }

    return error_found;
}

fn main() {
    let mut schema_directory = String::new();
    let mut sample_directory = String::new();
    {
        let mut parser = ArgumentParser::new();
        parser.refer(&mut schema_directory)
            .add_argument("schema-directory", Store, "Specify the directory of schemas to check");
        parser.refer(&mut sample_directory)
            .add_argument("sample-directory", Store, "Specify the directory of the samples to check");

        parser.parse_args_or_exit();
    }

    let validator_options = configure_validator::new(&schema_directory);
    if !check_samples(&schema_directory, &sample_directory, validator_options) {
        println!("Congratulations! No errors were found!");
    }
}
