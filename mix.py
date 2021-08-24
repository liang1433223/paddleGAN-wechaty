import subprocess


def gan1():
    cmd = "python -u E:/paddle套件/人脸融合/PaddleGAN/applications/tools/styleganv2fitting.py \
       --input_image image/first_image.png\
       --need_align \
       --start_lr 0.1 \
       --final_lr 0.025 \
       --latent_level 0 1 2 3 4 5 6 7 8 9 10 11 \
       --step 100 \
       --mse_weight 1 \
       --output_path output/1 \
       --model_type ffhq-config-f \
       --size 1024 \
       --style_dim 512 \
       --n_mlp 8 \
       --channel_multiplier 2"
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    result = out.split('\n')
    for lin in result:
        if not lin.startswith('#'):
            print(lin)


def gan2():
    cmd = "python -u E:/paddle套件/人脸融合/PaddleGAN/applications/tools/styleganv2fitting.py \
       --input_image image/2.png \
       --need_align \
       --start_lr 0.1 \
       --final_lr 0.025 \
       --latent_level 0 1 2 3 4 5 6 7 8 9 10 11 \
       --step 100 \
       --mse_weight 1 \
       --output_path output/2 \
       --model_type ffhq-config-f \
       --size 1024 \
       --style_dim 512 \
       --n_mlp 8 \
       --channel_multiplier 2"
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    result = out.split('\n')
    for lin in result:
        if not lin.startswith('#'):
            print(lin)


def mix_boy():
    cmd = "python -u E:/paddle套件/人脸融合/PaddleGAN/applications/tools/styleganv2mixing.py \
       --latent1 'output/1/dst.fitting.npy' \
       --latent2 'output/2/dst.fitting.npy' \
       --weights \
                 0.7 0.7 0.7 0.7 0.7 0.7 \
                 0.7 0.7 0.7 0.7 0.7 0.7 \
                 0.7 0.7 0.7 0.7 0.7 0.7 \
       --output_path 'mixoutput_boy/' \
       --model_type ffhq-config-f \
       --size 1024 \
       --style_dim 512 \
       --n_mlp 8 \
       --channel_multiplier 2 "
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    result = out.split('\n')
    for lin in result:
        if not lin.startswith('#'):
            print(lin)


def mix_girl():
    cmd = "python -u E:/paddle套件/人脸融合/PaddleGAN/applications/tools/styleganv2mixing.py \
       --latent1 'output/1/dst.fitting.npy' \
       --latent2 'output/2/dst.fitting.npy' \
       --weights \
                 0.3 0.3 0.3 0.3 0.3 0.3 \
                 0.3 0.3 0.3 0.3 0.3 0.3 \
                 0.3 0.3 0.3 0.3 0.3 0.3 \
       --output_path 'mixoutput_girl/' \
       --model_type ffhq-config-f \
       --size 1024 \
       --style_dim 512 \
       --n_mlp 8 \
       --channel_multiplier 2 "
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    result = out.split('\n')
    for lin in result:
        if not lin.startswith('#'):
            print(lin)
