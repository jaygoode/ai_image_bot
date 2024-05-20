from gradio_client import Client

client = Client("127.0.0.1:7865")
result = client.predict(
    False,  # bool in 'Disable Preview' Checkbox component
    0.1,  # int | float (numeric value between 0.1 and 3.0)
    0.1,  # int | float (numeric value between 0.1 and 3.0)
    0,  # int | float (numeric value between 0.0 and 1.0)
    1,  # int | float (numeric value between 1.0 and 30.0)	in 'CFG Mimicking from TSNR' Slider component
    "euler",  # str (Option from: ['euler', 'euler_ancestral', 'heun', 'heunpp2', 'dpm_2', 'dpm_2_ancestral', 'lms', 'dpm_fast', 'dpm_adaptive', 'dpmpp_2s_ancestral', 'dpmpp_sde', 'dpmpp_sde_gpu', 'dpmpp_2m', 'dpmpp_2m_sde', 'dpmpp_2m_sde_gpu', 'dpmpp_3m_sde', 'dpmpp_3m_sde_gpu', 'ddpm', 'lcm', 'ddim', 'uni_pc', 'uni_pc_bh2'])in 'Sampler' Dropdown component
    "normal",  # str (Option from: ['normal', 'karras', 'exponential', 'sgm_uniform', 'simple', 'ddim_uniform', 'lcm', 'turbo'])
    True,  # bool in 'Generate Image Grid for Each Batch' Checkbox component
    -1,  # int | f
    -1,  # int | fl
    -1,  # int | float (numeric value between -1 and 2048)
    -1,  # int | float (numeric value between -1 and 2048)
    -1,  # int | float (numeric value between -1 and 2048)
    -1,  # int | float (numeric value between -1 and 1.0)
    True,  # bool in 'Mixing Image Prompt and Vary/Upscale' Checkbox component
    True,  # bool in 'Mixing Image Prompt and Inpaint' Checkbox component
    True,  # bool in 'Debug Preprocessors' Checkbox component
    True,  # bool in 'Skip Preprocessors' Checkbox component
    0,  # int | float (numeric value between 0.0 and 1.0)
    1,  # int | float (numeric value between 1 and 255)
    1,  # int | float (numeric value between 1 and 255)
    "joint",  # str (Option from: ['joint', 'separate', 'vae'])
    True,  # bool in 'Enabled' Checkbox component
    0,  # int | float (numeric value between 0 and 2)
    0,  # int | float (numeric value between 0 and 2)
    0,  # int | float (numeric value between 0 and 4)
    0,  # int | float (numeric value between 0 and 4)
    True,  # bool in 'Debug Inpaint Preprocessing' Checkbox component
    True,  # bool in 'Disable initial latent in inpaint' Checkbox component
    "None",  # str (Option from: ['None', 'v1', 'v2.5', 'v2.6'])
    0,  # int | float (numeric value between 0.0 and 1.0)
    0,  # int | float (numeric value between 0.0 and 1.0)
    fn_index=29,
)
print(result)
