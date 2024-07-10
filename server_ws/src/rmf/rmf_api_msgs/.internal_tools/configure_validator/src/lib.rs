use jsonschema::{JSONSchema, CompilationOptions};
use serde_json::Value;

pub fn new(directory: &str) -> CompilationOptions {
    let mut options = JSONSchema::options();
    for entry in std::fs::read_dir(&directory).unwrap_or_else(|_| panic!("Failed to read from {}", &directory)) {
        let file = entry.unwrap();
        let schema_str = std::fs::read_to_string(&file.path()).unwrap();
        let schema: Value = serde_json::from_str(&schema_str)
            .unwrap_or_else(|err| panic!("Failed to parse {}: {}", file.path().to_str().unwrap(), err.to_string()));
        if let Value::Object(root) = &schema {
            if let Some(id_value) = root.get("$id") {
                if let Some(id) = id_value.as_str() {
                    options.with_document(id.to_string(), schema.clone());
                    continue;
                }
            }
        }

        // If the loop makes it here, then it failed to find an ID for this schema
        panic!("Missing id property for {}", file.path().to_str().unwrap());
    }

    return options;
}

#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        let result = 2 + 2;
        assert_eq!(result, 4);
    }
}
