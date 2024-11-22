How to download the HF model and run it in vllm 

1   pip install huggingface_hub

2   git config --global credential.helper store

3   huggingface-cli login

    need apply the token from the Hugging Face – The AI community building the future.
    
    https://huggingface.co/settings/tokens

4   huggingface-cli download NousResearch/Meta-Llama-3-8B-Instruct --local-dir model/Meta-Llama-3-8B-Instruct


4 run model

    in the vllm docker, run the serve like

    python -m vllm.entrypoints.openai.api_server --model model/huggingface/Meta-Llama-3-8B-Instruct --tensor-parallel-size 2
 
    python gradio_openai_chatbot_webserver.py --model model/huggingface/Meta-Llama-3-8B-Instruct

