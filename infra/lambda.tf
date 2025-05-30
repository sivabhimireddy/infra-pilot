resource "aws_iam_role" "lambda_exec" {
  name = "lambda_exec_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Action = "sts:AssumeRole",
      Effect = "Allow",
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}

resource "aws_lambda_function" "app" {
  function_name = "infra_pilot_lambda"
  role          = aws_iam_role.lambda_exec.arn
  runtime       = "python3.9"
  handler       = "lambda_function.lambda_handler"
  filename      = "lambda_function_payload.zip"
}
