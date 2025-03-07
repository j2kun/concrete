"""
Concrete.
"""

# pylint: disable=import-error,no-name-in-module

from concrete.compiler import EvaluationKeys, Parameter, PublicArguments, PublicResult

from .compilation import (
    DEFAULT_GLOBAL_P_ERROR,
    DEFAULT_P_ERROR,
    BitwiseStrategy,
    Circuit,
    Client,
    ClientSpecs,
    ComparisonStrategy,
    Compiler,
    Configuration,
    DebugArtifacts,
    EncryptionStatus,
    Keys,
    MinMaxStrategy,
    MultivariateStrategy,
    ParameterSelectionStrategy,
    Server,
    Value,
)
from .compilation.decorators import circuit, compiler
from .extensions import (
    AutoRounder,
    LookupTable,
    array,
    conv,
    hint,
    maxpool,
    multivariate,
    one,
    ones,
    ones_like,
    round_bit_pattern,
    tag,
    univariate,
    zero,
    zeros,
    zeros_like,
)
from .mlir.utils import MAXIMUM_TLU_BIT_WIDTH
from .representation import Graph
from .tracing.typing import (
    f32,
    f64,
    int1,
    int2,
    int3,
    int4,
    int5,
    int6,
    int7,
    int8,
    int9,
    int10,
    int11,
    int12,
    int13,
    int14,
    int15,
    int16,
    int17,
    int18,
    int19,
    int20,
    int21,
    int22,
    int23,
    int24,
    int25,
    int26,
    int27,
    int28,
    int29,
    int30,
    int31,
    int32,
    int33,
    int34,
    int35,
    int36,
    int37,
    int38,
    int39,
    int40,
    int41,
    int42,
    int43,
    int44,
    int45,
    int46,
    int47,
    int48,
    int49,
    int50,
    int51,
    int52,
    int53,
    int54,
    int55,
    int56,
    int57,
    int58,
    int59,
    int60,
    int61,
    int62,
    int63,
    int64,
    tensor,
    uint1,
    uint2,
    uint3,
    uint4,
    uint5,
    uint6,
    uint7,
    uint8,
    uint9,
    uint10,
    uint11,
    uint12,
    uint13,
    uint14,
    uint15,
    uint16,
    uint17,
    uint18,
    uint19,
    uint20,
    uint21,
    uint22,
    uint23,
    uint24,
    uint25,
    uint26,
    uint27,
    uint28,
    uint29,
    uint30,
    uint31,
    uint32,
    uint33,
    uint34,
    uint35,
    uint36,
    uint37,
    uint38,
    uint39,
    uint40,
    uint41,
    uint42,
    uint43,
    uint44,
    uint45,
    uint46,
    uint47,
    uint48,
    uint49,
    uint50,
    uint51,
    uint52,
    uint53,
    uint54,
    uint55,
    uint56,
    uint57,
    uint58,
    uint59,
    uint60,
    uint61,
    uint62,
    uint63,
    uint64,
)
from .version import __version__

# pylint: enable=import-error,no-name-in-module
