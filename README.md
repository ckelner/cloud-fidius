# Cloud Fidius
A tool to reconcile what is running in your cloud environment and compare it to
what you expect to be running in that environment.

# Getting Started

## Requirements
- Python 2 (2.6.7)

## Config
Set up credentials in ``~/.aws/credentials``:

```ini
    [default]
    aws_access_key_id = YOUR_KEY
    aws_secret_access_key = YOUR_SECRET
```

Then, set up a default region in ``~/.aws/config``:

```ini
    [default]
    region=us-east-1
```
