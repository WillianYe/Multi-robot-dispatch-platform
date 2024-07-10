This workspace contains tools that are used internally for inspecting the RMF API.

These tools are built using Rust and Cargo, so you will need to [install those](https://doc.rust-lang.org/cargo/getting-started/installation.html) to use these tools.

## Checking the validity of the schemas

To ensure that the schemas themselves in `rmf_api_msgs` do not contain errors, we have a CLI tool called `check_schemas`.

From this Cargo workspace directory, run the command

```
$ cargo run -p check_schemas -- ../rmf_api_msgs/schemas
```

If all the schemas were successfully compiled, you will see the message:

```
Congratulations! No errors were found!
```

Otherwise you will see a list of error messages describing the problems that were detected in the schemas.

## Checking the validity of the samples

The `check_samples` tool can verify that the sample messages that are provided in `rmf_api_msgs` comply with their respective schemas. From this Cargo workspace directory, run the command

```
$ cargo run -p check_samples -- ../rmf_api_msgs/schemas ../rmf_api_msgs/samples
```

If all the samples are valid, you will see the message:

```
Congratulations! No errors were found!
```

Otherwise you will see a list of error messages describing the problems that were detected in the samples.
