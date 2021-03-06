# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.dipy.tensors import TensorMode

def test_TensorMode_inputs():
    input_map = dict(bvals=dict(mandatory=True,
    ),
    bvecs=dict(mandatory=True,
    ),
    in_file=dict(mandatory=True,
    ),
    out_filename=dict(genfile=True,
    ),
    )
    inputs = TensorMode.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_TensorMode_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = TensorMode.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

