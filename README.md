How to download the HF model and run it in vllm 

1   pip install huggingface_hub

2   git config --global credential.helper store

3   huggingface-cli login

    need apply the token from the Hugging Face – The AI community building the future.
    
    https://huggingface.co/settings/tokens

4   huggingface-cli download Qwen/Qwen2.5-7B-Instruct --local-dir model/Qwen2.5-7B-Instruct

5   build the Rocm docker

    git clone https://github.com/vllm-project/vllm.git

    cd vllm

    DOCKER_BUILDKIT=1 docker build -f Dockerfile.rocm -t vllm-rocm .

6   Run the vllm docker

    docker run -it \
    --network=host \
    --group-add=video \
    --ipc=host \
    --cap-add=SYS_PTRACE \
    --security-opt seccomp=unconfined \
    --device /dev/kfd \
    --device /dev/dri \
    -v /home/minx/Documents/vllm/model/Qwen2.5-7B-Instruct:/workspace/Qwen2.5-7B-Instruct \
    vllm-rocm \
    bash
    


7 run model

    in the vllm docker, run the serve like

    python -m vllm.entrypoints.openai.api_server --model /workspace/Qwen2.5-7B-Instruct --tensor-parallel-size 2
 
    python gradio_openai_chatbot_webserver.py --model /workspace/Qwen2.5-7B-Instruct


8 test  

    #>curl http://localhost:8000/v1/models
    {"object":"list","data":[{"id":"/workspace/Qwen2.5-7B-Instruct","object":"model","created":1732268408,"owned_by":"vllm","root":"/workspace/Qwen2.5-7B-Instruct","parent":null,"max_model_len":32768,"permission":[{"id":"modelperm-0c316cdfead64a9599b824b66ab89f18","object":"model_permission","created":1732268408,"allow_create_engine":false,"allow_sampling":true,"allow_logprobs":true,"allow_search_indices":false,"allow_view":true,"allow_fine_tuning":false,"or

