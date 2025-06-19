module "vpc" {
  source = "./modules/vpc"
}

module "eks" {
  source = "./modules/eks"
}

module "rds" {
  source = "./modules/rds"
}

module "redis" {
  source = "./modules/redis"
}

module "s3" {
  source = "./modules/s3"
}

module "acm" {
  source = "./modules/acm"
}

module "kms" {
  source = "./modules/kms"
}

module "waf" {
  source = "./modules/waf"
}
