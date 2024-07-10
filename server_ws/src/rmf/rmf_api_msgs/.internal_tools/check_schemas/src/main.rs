use argparse::{ArgumentParser, Store};
use jsonschema::CompilationOptions;
use serde_json::Value;
use configure_validator;

fn attempt_compile(directory: &str, options: CompilationOptions) -> bool {
    let mut error_found = false;
    for entry in std::fs::read_dir(&directory).unwrap() {
        let file = entry.unwrap();
        let schema_str = std::fs::read_to_string(&file.path()).unwrap();
        let schema: Value = serde_json::from_str(&schema_str).unwrap();
        if let Err(err) = options.compile(&schema) {
            println!("Error in {}: {}", file.path().to_str().unwrap(), err.to_string());
            error_found = true;
        }
    }

    return error_found;
}

fn main() {
    let mut directory = String::new();
    {
        let mut parser = ArgumentParser::new();
        parser.refer(&mut directory)
            .add_argument("schema-directory", Store, "Specify the directory of schemas to check");

        parser.parse_args_or_exit();
    }

    let validator_options = configure_validator::new(&directory);
    if !attempt_compile(&directory, validator_options) {
        println!("Congratulations! No errors were found!");
    }
}
