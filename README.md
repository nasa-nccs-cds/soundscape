# soundscape
Platform for experimentation with Machine Learning methods using audio data

### Conda Environment Setup

    >  conda create --name sscape -c conda-forge 
    >  conda activate sscape  
    >  conda install pytorch::pytorch torchvision torchaudio -c pytorch 
    >  conda install -c conda-forge wandb apex ruamel timm einops cdsapi h5py mpi4py netCDF4 matplotlib
    > pip install hydra-core --upgrade