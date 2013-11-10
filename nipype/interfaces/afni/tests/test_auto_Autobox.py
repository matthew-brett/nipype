# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.afni.preprocess import Autobox
def test_Autobox_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    out_file=dict(name_source='in_file',
    argstr='-prefix %s',
    ),
    args=dict(argstr='%s',
    ),
    outputtype=dict(),
    padding=dict(argstr='-npad %d',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(mandatory=True,
    argstr='-input %s',
    ),
    no_clustering=dict(argstr='-noclust',
    ),
    )
    inputs = Autobox.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_Autobox_outputs():
    output_map = dict(y_min=dict(),
    y_max=dict(),
    z_max=dict(),
    z_min=dict(),
    x_max=dict(),
    x_min=dict(),
    out_file=dict(),
    )
    outputs = Autobox.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value