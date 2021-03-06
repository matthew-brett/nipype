# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.afni.preprocess import Bandpass

def test_Bandpass_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    automask=dict(argstr='-automask',
    ),
    blur=dict(argstr='-blur %f',
    ),
    despike=dict(argstr='-despike',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    highpass=dict(argstr='%f',
    mandatory=True,
    position=-3,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    copyfile=False,
    mandatory=True,
    position=-1,
    ),
    localPV=dict(argstr='-localPV %f',
    ),
    lowpass=dict(argstr='%f',
    mandatory=True,
    position=-2,
    ),
    mask=dict(argstr='-mask %s',
    position=2,
    ),
    nfft=dict(argstr='-nfft %d',
    ),
    no_detrend=dict(argstr='-nodetrend',
    ),
    normalize=dict(argstr='-norm',
    ),
    notrans=dict(argstr='-notrans',
    ),
    orthogonalize_dset=dict(argstr='-dsort %s',
    ),
    orthogonalize_file=dict(argstr='-ort %s',
    ),
    out_file=dict(argstr='-prefix %s',
    genfile=True,
    name_source='in_file',
    name_template='%s_bp',
    position=1,
    ),
    outputtype=dict(),
    terminal_output=dict(nohash=True,
    ),
    tr=dict(argstr='-dt %f',
    ),
    )
    inputs = Bandpass.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_Bandpass_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = Bandpass.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

