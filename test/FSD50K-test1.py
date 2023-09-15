from sscape.util.conf import configure, cfg
from glob import glob
from pathlib import Path
from sscape.util.plot import plot_waveform
import torchaudio
config_name = "FSD50K-local-test1"
mode = "dev"

if __name__ == "__main__":
    configure( config_name )
    data_dir = f"{cfg().platform.data_dir}/{cfg().platform.dataset}"
    data_files = glob( f"{data_dir}/{mode}/*.wav")

    metadata = torchaudio.info(data_files[0])
    waveform, sample_rate = torchaudio.load(data_files[0])

    print(f" {Path(data_files[0]).stem}: {metadata} {waveform}")

    plot_waveform( waveform, sample_rate )