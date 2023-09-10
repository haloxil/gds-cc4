provider "aws" {
  region = "ap-southeast-1" 
  # Configure your own AWS access and secret key and save it in $HOME/.aws/credentials
}

resource "aws_s3_bucket" "govtech_bucket" {
  bucket = "govtech-cc4"
}