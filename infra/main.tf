provider "aws" {
  region = var.region
}

# VPC and networking
module "vpc" {
  source = "./vpc.tf"
}

# EKS cluster
module "eks" {
  source = "./eks.tf"
}

# Application Load Balancer
module "alb" {
  source = "./alb.tf"
}

# RDS Database
module "rds" {
  source = "./rds.tf"
}

# Lambda function
module "lambda" {
  source = "./lambda.tf"
}

# IAM roles/policies
module "iam" {
  source = "./iam.tf"
}
