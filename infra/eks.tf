module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  cluster_name    = "demo-eks"
  cluster_version = "1.24"
  subnet_ids      = [aws_subnet.public.id]
  vpc_id          = aws_vpc.main.id
  enable_irsa     = true
}
