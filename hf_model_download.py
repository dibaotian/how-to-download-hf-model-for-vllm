from transformers import AutoModel, AutoTokenizer

# 例如使用一个模型名称
model_name = "Qwen/Qwen2.5-7B-Instruct" 

# 下载模型和分词器到本地路径
model = AutoModel.from_pretrained(model_name, cache_dir="../")
tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir="../")


# Make sure you have git-lfs installed (https://git-lfs.com)
git lfs install

git clone https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct

# If you want to clone without large files - just their pointers
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/Qwen/Qwen2.5-Coder-32B-I

