output "vpc_id" {
  value = aws_vpc.main.id
}

output "eks_cluster_name" {
  value = module.eks.cluster_name
}
