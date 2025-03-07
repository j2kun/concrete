<!-- Autogenerated by mlir-tblgen; don't manually edit -->
# 'FHE' Dialect

High Level Fully Homomorphic Encryption dialect
A dialect for representation of high level operation on fully homomorphic ciphertext.



## Operation definition

### `FHE.add_eint_int` (::mlir::concretelang::FHE::AddEintIntOp)

Adds an encrypted integer and a clear integer

The clear integer must have at most one more bit than the encrypted integer
and the result must have the same width and the same signedness as the encrypted integer.

Example:
```mlir
// ok
"FHE.add_eint_int"(%a, %i) : (!FHE.eint<2>, i3) -> !FHE.eint<2>
"FHE.add_eint_int"(%a, %i) : (!FHE.esint<2>, i3) -> !FHE.esint<2>

// error
"FHE.add_eint_int"(%a, %i) : (!FHE.eint<2>, i4) -> !FHE.eint<2>
"FHE.add_eint_int"(%a, %i) : (!FHE.eint<2>, i3) -> !FHE.eint<3>
"FHE.add_eint_int"(%a, %i) : (!FHE.eint<2>, i3) -> !FHE.esint<2>
```

Traits: AlwaysSpeculatableImplTrait

Interfaces: Binary, BinaryEintInt, ConditionallySpeculatable, NoMemoryEffect (MemoryEffectOpInterface)

Effects: MemoryEffects::Effect{}

#### Operands:

| Operand | Description |
| :-----: | ----------- |
| `a` | 
| `b` | integer

#### Results:

| Result | Description |
| :----: | ----------- |
&laquo;unnamed&raquo; | 

### `FHE.add_eint` (::mlir::concretelang::FHE::AddEintOp)

Adds two encrypted integers

The encrypted integers and the result must have the same width and the same signedness.

Example:
```mlir
// ok
"FHE.add_eint"(%a, %b): (!FHE.eint<2>, !FHE.eint<2>) -> (!FHE.eint<2>)
"FHE.add_eint"(%a, %b): (!FHE.esint<2>, !FHE.esint<2>) -> (!FHE.esint<2>)

// error
"FHE.add_eint"(%a, %b): (!FHE.eint<2>, !FHE.eint<3>) -> (!FHE.eint<2>)
"FHE.add_eint"(%a, %b): (!FHE.eint<2>, !FHE.eint<2>) -> (!FHE.eint<3>)
"FHE.add_eint"(%a, %b): (!FHE.eint<2>, !FHE.eint<2>) -> (!FHE.esint<2>)
"FHE.add_eint"(%a, %b): (!FHE.esint<2>, !FHE.eint<2>) -> (!FHE.eint<2>)
```

Traits: AlwaysSpeculatableImplTrait

Interfaces: BinaryEint, ConditionallySpeculatable, NoMemoryEffect (MemoryEffectOpInterface)

Effects: MemoryEffects::Effect{}

#### Operands:

| Operand | Description |
| :-----: | ----------- |
| `a` | 
| `b` | 

#### Results:

| Result | Description |
| :----: | ----------- |
&laquo;unnamed&raquo; | 

### `FHE.apply_lookup_table` (::mlir::concretelang::FHE::ApplyLookupTableEintOp)

Applies a clear lookup table to an encrypted integer

The width of the result can be different than the width of the operand.
The lookup table must be a tensor of size `2^p` where `p` is the width of the encrypted integer.

Example:
```mlir
// ok
"FHE.apply_lookup_table"(%a, %lut): (!FHE.eint<2>, tensor<4xi64>) -> (!FHE.eint<2>)
"FHE.apply_lookup_table"(%a, %lut): (!FHE.eint<2>, tensor<4xi64>) -> (!FHE.eint<3>)
"FHE.apply_lookup_table"(%a, %lut): (!FHE.eint<3>, tensor<4xi64>) -> (!FHE.eint<2>)

// error
"FHE.apply_lookup_table"(%a, %lut): (!FHE.eint<2>, tensor<8xi64>) -> (!FHE.eint<2>)
```

Traits: AlwaysSpeculatableImplTrait

Interfaces: ConditionallySpeculatable, ConstantNoise, NoMemoryEffect (MemoryEffectOpInterface)

Effects: MemoryEffects::Effect{}

#### Operands:

| Operand | Description |
| :-----: | ----------- |
| `a` | 
| `lut` | tensor of integer values

#### Results:

| Result | Description |
| :----: | ----------- |
&laquo;unnamed&raquo; | 

### `FHE.and` (::mlir::concretelang::FHE::BoolAndOp)

Applies an AND gate to two encrypted boolean values

Example:
```mlir
"FHE.and"(%a, %b): (!FHE.ebool, !FHE.ebool) -> (!FHE.ebool)
```

Traits: AlwaysSpeculatableImplTrait

Interfaces: ConditionallySpeculatable, NoMemoryEffect (MemoryEffectOpInterface)

Effects: MemoryEffects::Effect{}

#### Operands:

| Operand | Description |
| :-----: | ----------- |
| `left` | An encrypted boolean
| `right` | An encrypted boolean

#### Results:

| Result | Description |
| :----: | ----------- |
&laquo;unnamed&raquo; | An encrypted boolean

### `FHE.nand` (::mlir::concretelang::FHE::BoolNandOp)

Applies a NAND gate to two encrypted boolean values

Example:
```mlir
"FHE.nand"(%a, %b): (!FHE.ebool, !FHE.ebool) -> (!FHE.ebool)
```

Traits: AlwaysSpeculatableImplTrait

Interfaces: ConditionallySpeculatable, NoMemoryEffect (MemoryEffectOpInterface)

Effects: MemoryEffects::Effect{}

#### Operands:

| Operand | Description |
| :-----: | ----------- |
| `left` | An encrypted boolean
| `right` | An encrypted boolean

#### Results:

| Result | Description |
| :----: | ----------- |
&laquo;unnamed&raquo; | An encrypted boolean

### `FHE.not` (::mlir::concretelang::FHE::BoolNotOp)

Applies a NOT gate to an encrypted boolean value

Example:
```mlir
"FHE.not"(%a): (!FHE.ebool) -> (!FHE.ebool)
```

Traits: AlwaysSpeculatableImplTrait

Interfaces: ConditionallySpeculatable, NoMemoryEffect (MemoryEffectOpInterface), UnaryEint

Effects: MemoryEffects::Effect{}

#### Operands:

| Operand | Description |
| :-----: | ----------- |
| `value` | An encrypted boolean

#### Results:

| Result | Description |
| :----: | ----------- |
&laquo;unnamed&raquo; | An encrypted boolean

### `FHE.or` (::mlir::concretelang::FHE::BoolOrOp)

Applies an OR gate to two encrypted boolean values

Example:
```mlir
"FHE.or"(%a, %b): (!FHE.ebool, !FHE.ebool) -> (!FHE.ebool)
```

Traits: AlwaysSpeculatableImplTrait

Interfaces: ConditionallySpeculatable, NoMemoryEffect (MemoryEffectOpInterface)

Effects: MemoryEffects::Effect{}

#### Operands:

| Operand | Description |
| :-----: | ----------- |
| `left` | An encrypted boolean
| `right` | An encrypted boolean

#### Results:

| Result | Description |
| :----: | ----------- |
&laquo;unnamed&raquo; | An encrypted boolean

### `FHE.xor` (::mlir::concretelang::FHE::BoolXorOp)

Applies an XOR gate to two encrypted boolean values

Example:
```mlir
"FHE.xor"(%a, %b): (!FHE.ebool, !FHE.ebool) -> (!FHE.ebool)
```

Traits: AlwaysSpeculatableImplTrait

Interfaces: ConditionallySpeculatable, NoMemoryEffect (MemoryEffectOpInterface)

Effects: MemoryEffects::Effect{}

#### Operands:

| Operand | Description |
| :-----: | ----------- |
| `left` | An encrypted boolean
| `right` | An encrypted boolean

#### Results:

| Result | Description |
| :----: | ----------- |
&laquo;unnamed&raquo; | An encrypted boolean

### `FHE.from_bool` (::mlir::concretelang::FHE::FromBoolOp)

Cast a boolean to an unsigned integer

Examples:
```mlir
"FHE.from_bool"(%x) : (!FHE.ebool) -> !FHE.eint<1>
"FHE.from_bool"(%x) : (!FHE.ebool) -> !FHE.eint<2>
"FHE.from_bool"(%x) : (!FHE.ebool) -> !FHE.eint<4>
```

Traits: AlwaysSpeculatableImplTrait

Interfaces: ConditionallySpeculatable, NoMemoryEffect (MemoryEffectOpInterface), UnaryEint

Effects: MemoryEffects::Effect{}

#### Operands:

| Operand | Description |
| :-----: | ----------- |
| `input` | An encrypted boolean

#### Results:

| Result | Description |
| :----: | ----------- |
&laquo;unnamed&raquo; | An encrypted unsigned integer

### `FHE.gen_gate` (::mlir::concretelang::FHE::GenGateOp)

Applies a truth table based on two boolean inputs

Truth table must be a tensor of four boolean values.

Example:
```mlir
// ok
"FHE.gen_gate"(%a, %b, %ttable): (!FHE.ebool, !FHE.ebool, tensor<4xi64>) -> (!FHE.ebool)

// error
"FHE.gen_gate"(%a, %b, %ttable): (!FHE.ebool, !FHE.ebool, tensor<7xi64>) -> (!FHE.ebool)
```

Traits: AlwaysSpeculatableImplTrait

Interfaces: ConditionallySpeculatable, NoMemoryEffect (MemoryEffectOpInterface)

Effects: MemoryEffects::Effect{}

#### Operands:

| Operand | Description |
| :-----: | ----------- |
| `left` | An encrypted boolean
| `right` | An encrypted boolean
| `truth_table` | tensor of integer values

#### Results:

| Result | Description |
| :----: | ----------- |
&laquo;unnamed&raquo; | An encrypted boolean

### `FHE.lsb` (::mlir::concretelang::FHE::LsbEintOp)

Extract the lowest significant bit at a given precision.

  This operation extract the lsb of a ciphertext in a specific precision.

  Extracting the lsb with the smallest precision:
  ```mlir
   // Checking if even or odd
   %even = "FHE.lsb"(%a): (!FHE.eint<4>) -> (!FHE.eint<1>)

  Usually when you extract the lsb bit, you also need to extract the next one.
  In that case you first need to clear the first lsb of the input to be able to reduce its precision and extract the next one.
  To be able to clear the lsb just extracted, you can get it in the original precision.

  Example:
  ```mlir
   // Extracting the first lsb with original precision
   %lsb_0 = "FHE.lsb"(%input): (!FHE.eint<4>) -> (!FHE.eint<4>)
   // Clearing the first lsb from original input
   %input_lsb0_cleared = "FHE.sub_eint"(%input, %lsb_0) : (!FHE.eint<4>, !FHE.eint<4>) -> (!FHE.eint<4>)
   // Reducing the precision of the input
   %input_3b = "FHE.reinterpret_precision(%input) : (!FHE.eint<4>) -> !FHE.eint<3>
   // Now, we can do it again with the second lsb
   %lsb_1 = "FHE.lsb"(%input_3b): (!FHE.eint<3>) -> (!FHE.eint<3>)
   ...
   // later if you need %b_lsb at same position as in the input
   %lsb_1_at_input_position = "FHE.reinterpret_precision(%b_lsb)" : (!FHE.eint<3>) -> !FHE.eint<4>
   // that way you can recombine the extracted bits
   %input_mod_4 = "FHE.add_eint"(%lsb_0, %lsb_1_at_input_position) : (!FHE.eint<4>, !FHE.eint<4>) -> (!FHE.eint<4>)
```

Traits: AlwaysSpeculatableImplTrait

Interfaces: ConditionallySpeculatable, ConstantNoise, NoMemoryEffect (MemoryEffectOpInterface), UnaryEint

Effects: MemoryEffects::Effect{}

#### Operands:

| Operand | Description |
| :-----: | ----------- |
| `input` | 

#### Results:

| Result | Description |
| :----: | ----------- |
&laquo;unnamed&raquo; | 

### `FHE.max_eint` (::mlir::concretelang::FHE::MaxEintOp)

Retrieve the maximum of two encrypted integers.

Retrieve the maximum of two encrypted integers using the formula, 'max(x, y) == max(x - y, 0) + y'.
The input and output types should be the same.

If `x - y`` inside the max overflows or underflows, the behavior is undefined.
To support the full range, you should increase the bit-width by 1 manually.

Example:
```mlir
// ok
"FHE.max_eint"(%x, %y) : (!FHE.eint<2>, !FHE.eint<2>) -> !FHE.eint<2>
"FHE.max_eint"(%x, %y) : (!FHE.esint<3>, !FHE.esint<3>) -> !FHE.esint<3>

// error
"FHE.max_eint"(%x, %y) : (!FHE.eint<2>, !FHE.eint<3>) -> !FHE.eint<2>
"FHE.max_eint"(%x, %y) : (!FHE.eint<2>, !FHE.eint<2>) -> !FHE.esint<2>
"FHE.max_eint"(%x, %y) : (!FHE.esint<2>, !FHE.eint<2>) -> !FHE.eint<2>
```

Traits: AlwaysSpeculatableImplTrait

Interfaces: BinaryEint, ConditionallySpeculatable, NoMemoryEffect (MemoryEffectOpInterface)

Effects: MemoryEffects::Effect{}

#### Operands:

| Operand | Description |
| :-----: | ----------- |
| `x` | 
| `y` | 

#### Results:

| Result | Description |
| :----: | ----------- |
&laquo;unnamed&raquo; | 

### `FHE.mul_eint_int` (::mlir::concretelang::FHE::MulEintIntOp)

Multiply an encrypted integer with a clear integer

The clear integer must have one more bit than the encrypted integer
and the result must have the same width and the same signedness as the encrypted integer.

Example:
```mlir
// ok
"FHE.mul_eint_int"(%a, %i) : (!FHE.eint<2>, i3) -> !FHE.eint<2>
"FHE.mul_eint_int"(%a, %i) : (!FHE.esint<2>, i3) -> !FHE.esint<2>

// error
"FHE.mul_eint_int"(%a, %i) : (!FHE.eint<2>, i4) -> !FHE.eint<2>
"FHE.mul_eint_int"(%a, %i) : (!FHE.eint<2>, i3) -> !FHE.eint<3>
"FHE.mul_eint_int"(%a, %i) : (!FHE.eint<2>, i3) -> !FHE.esint<2>
```

Traits: AlwaysSpeculatableImplTrait

Interfaces: Binary, BinaryEintInt, ConditionallySpeculatable, NoMemoryEffect (MemoryEffectOpInterface)

Effects: MemoryEffects::Effect{}

#### Operands:

| Operand | Description |
| :-----: | ----------- |
| `a` | 
| `b` | integer

#### Results:

| Result | Description |
| :----: | ----------- |
&laquo;unnamed&raquo; | 

### `FHE.mul_eint` (::mlir::concretelang::FHE::MulEintOp)

Multiplies two encrypted integers

The encrypted integers and the result must have the same width and
signedness. Also, due to the current implementation, one supplementary
bit of width must be provided, in addition to the number of bits needed
to encode the largest output value.

Example:
```mlir
// ok
"FHE.mul_eint"(%a, %b): (!FHE.eint<2>, !FHE.eint<2>) -> (!FHE.eint<2>)
"FHE.mul_eint"(%a, %b): (!FHE.eint<3>, !FHE.eint<3>) -> (!FHE.eint<3>)
"FHE.mul_eint"(%a, %b): (!FHE.esint<3>, !FHE.esint<3>) -> (!FHE.esint<3>)

// error
"FHE.mul_eint"(%a, %b): (!FHE.eint<2>, !FHE.eint<3>) -> (!FHE.eint<2>)
"FHE.mul_eint"(%a, %b): (!FHE.eint<2>, !FHE.eint<2>) -> (!FHE.eint<3>)
"FHE.mul_eint"(%a, %b): (!FHE.eint<2>, !FHE.eint<2>) -> (!FHE.esint<2>)
"FHE.mul_eint"(%a, %b): (!FHE.esint<2>, !FHE.eint<2>) -> (!FHE.eint<2>)
```

Traits: AlwaysSpeculatableImplTrait

Interfaces: BinaryEint, ConditionallySpeculatable, NoMemoryEffect (MemoryEffectOpInterface)

Effects: MemoryEffects::Effect{}

#### Operands:

| Operand | Description |
| :-----: | ----------- |
| `rhs` | 
| `lhs` | 

#### Results:

| Result | Description |
| :----: | ----------- |
&laquo;unnamed&raquo; | 

### `FHE.mux` (::mlir::concretelang::FHE::MuxOp)

Multiplexer for two encrypted boolean inputs, based on an encrypted condition

Example:
```mlir
"FHE.mux"(%cond, %c1, %c2): (!FHE.ebool, !FHE.ebool, !FHE.ebool) -> (!FHE.ebool)
```

Traits: AlwaysSpeculatableImplTrait

Interfaces: ConditionallySpeculatable, NoMemoryEffect (MemoryEffectOpInterface)

Effects: MemoryEffects::Effect{}

#### Operands:

| Operand | Description |
| :-----: | ----------- |
| `cond` | An encrypted boolean
| `c1` | An encrypted boolean
| `c2` | An encrypted boolean

#### Results:

| Result | Description |
| :----: | ----------- |
&laquo;unnamed&raquo; | An encrypted boolean

### `FHE.neg_eint` (::mlir::concretelang::FHE::NegEintOp)

Negates an encrypted integer

The result must have the same width and the same signedness as the encrypted integer.

Example:
```mlir
// ok
"FHE.neg_eint"(%a): (!FHE.eint<2>) -> (!FHE.eint<2>)
"FHE.neg_eint"(%a): (!FHE.esint<2>) -> (!FHE.esint<2>)

// error
"FHE.neg_eint"(%a): (!FHE.eint<2>) -> (!FHE.eint<3>)
"FHE.neg_eint"(%a): (!FHE.eint<2>) -> (!FHE.esint<2>)
```

Traits: AlwaysSpeculatableImplTrait

Interfaces: ConditionallySpeculatable, NoMemoryEffect (MemoryEffectOpInterface), UnaryEint

Effects: MemoryEffects::Effect{}

#### Operands:

| Operand | Description |
| :-----: | ----------- |
| `a` | 

#### Results:

| Result | Description |
| :----: | ----------- |
&laquo;unnamed&raquo; | 

### `FHE.reinterpret_precision` (::mlir::concretelang::FHE::ReinterpretPrecisionEintOp)

Reinterpret the ciphertext with a different precision.

  Changing the precision of a ciphertext.
  It change both the precision, the value and in certain case the correctness of the cyphertext.

  Changing to
    - a bigger precision is always safe.
      This is equivalent to a shift left for the value
    - a smaller precision is only safe if you clear the lowest bits that are discarded.
      If not, you can assume small errors on the next TLU.
      This is equivalent to a shift right for the value

  Example:
  ```mlir
   // assuming %a is stored as 4bits but can be stored with only 2bits
   // we can reduce its storage precision
   %shifted_a = "FHE.mul_eint_int"(%a, %c_4): (!FHE.eint<4>) -> (!FHE.eint<4>)
   %a_small_precision = "FHE.reinterpret_precision"(%shifted_a, %lsb) : (!FHE.eint<4>) -> (!FHE.eint<2>)
```

Traits: AlwaysSpeculatableImplTrait

Interfaces: ConditionallySpeculatable, NoMemoryEffect (MemoryEffectOpInterface), UnaryEint

Effects: MemoryEffects::Effect{}

#### Operands:

| Operand | Description |
| :-----: | ----------- |
| `input` | 

#### Results:

| Result | Description |
| :----: | ----------- |
&laquo;unnamed&raquo; | 

### `FHE.round` (::mlir::concretelang::FHE::RoundEintOp)

Rounds a ciphertext to a smaller precision.

  Assuming a ciphertext whose message is implemented over `p` bits, this
      operation rounds it to fit to `q` bits with `p>q`.

  Example:
  ```mlir
   // ok
   "FHE.round"(%a): (!FHE.eint<6>) -> (!FHE.eint<5>)
   "FHE.round"(%a): (!FHE.eint<5>) -> (!FHE.eint<3>)
   "FHE.round"(%a): (!FHE.eint<3>) -> (!FHE.eint<2>)
   "FHE.round"(%a): (!FHE.esint<3>) -> (!FHE.esint<2>)

// error
   "FHE.round"(%a): (!FHE.eint<6>) -> (!FHE.eint<6>)
   "FHE.round"(%a): (!FHE.eint<4>) -> (!FHE.eint<5>)
   "FHE.round"(%a): (!FHE.eint<4>) -> (!FHE.esint<5>)

```

Traits: AlwaysSpeculatableImplTrait

Interfaces: ConditionallySpeculatable, NoMemoryEffect (MemoryEffectOpInterface), UnaryEint

Effects: MemoryEffects::Effect{}

#### Operands:

| Operand | Description |
| :-----: | ----------- |
| `input` | 

#### Results:

| Result | Description |
| :----: | ----------- |
&laquo;unnamed&raquo; | 

### `FHE.sub_eint_int` (::mlir::concretelang::FHE::SubEintIntOp)

Subtract a clear integer from an encrypted integer

The clear integer must have one more bit than the encrypted integer
and the result must have the same width and the same signedness as the encrypted integer.

Example:
```mlir
// ok
"FHE.sub_eint_int"(%i, %a) : (!FHE.eint<2>, i3) -> !FHE.eint<2>
"FHE.sub_eint_int"(%i, %a) : (!FHE.esint<2>, i3) -> !FHE.esint<2>

// error
"FHE.sub_eint_int"(%i, %a) : (!FHE.eint<2>, i4) -> !FHE.eint<2>
"FHE.sub_eint_int"(%i, %a) : (!FHE.eint<2>, i3) -> !FHE.eint<3>
"FHE.sub_eint_int"(%i, %a) : (!FHE.eint<2>, i3) -> !FHE.esint<2>
```

Traits: AlwaysSpeculatableImplTrait

Interfaces: Binary, BinaryEintInt, ConditionallySpeculatable, NoMemoryEffect (MemoryEffectOpInterface)

Effects: MemoryEffects::Effect{}

#### Operands:

| Operand | Description |
| :-----: | ----------- |
| `a` | 
| `b` | integer

#### Results:

| Result | Description |
| :----: | ----------- |
&laquo;unnamed&raquo; | 

### `FHE.sub_eint` (::mlir::concretelang::FHE::SubEintOp)

Subtract an encrypted integer from an encrypted integer

The encrypted integers and the result must have the same width and the same signedness.

Example:
```mlir
// ok
"FHE.sub_eint"(%a, %b): (!FHE.eint<2>, !FHE.eint<2>) -> (!FHE.eint<2>)
"FHE.sub_eint"(%a, %b): (!FHE.esint<2>, !FHE.esint<2>) -> (!FHE.esint<2>)

// error
"FHE.sub_eint"(%a, %b): (!FHE.eint<2>, !FHE.eint<3>) -> (!FHE.eint<2>)
"FHE.sub_eint"(%a, %b): (!FHE.eint<2>, !FHE.eint<2>) -> (!FHE.eint<3>)
"FHE.sub_eint"(%a, %b): (!FHE.eint<2>, !FHE.esint<2>) -> (!FHE.esint<2>)
"FHE.sub_eint"(%a, %b): (!FHE.eint<2>, !FHE.eint<2>) -> (!FHE.esint<2>)
```

Traits: AlwaysSpeculatableImplTrait

Interfaces: BinaryEint, ConditionallySpeculatable, NoMemoryEffect (MemoryEffectOpInterface)

Effects: MemoryEffects::Effect{}

#### Operands:

| Operand | Description |
| :-----: | ----------- |
| `a` | 
| `b` | 

#### Results:

| Result | Description |
| :----: | ----------- |
&laquo;unnamed&raquo; | 

### `FHE.sub_int_eint` (::mlir::concretelang::FHE::SubIntEintOp)

Subtract an encrypted integer from a clear integer

The clear integer must have one more bit than the encrypted integer
and the result must have the same width and the same signedness as the encrypted integer.

Example:
```mlir
// ok
"FHE.sub_int_eint"(%i, %a) : (i3, !FHE.eint<2>) -> !FHE.eint<2>
"FHE.sub_int_eint"(%i, %a) : (i3, !FHE.esint<2>) -> !FHE.esint<2>

// error
"FHE.sub_int_eint"(%i, %a) : (i4, !FHE.eint<2>) -> !FHE.eint<2>
"FHE.sub_int_eint"(%i, %a) : (i3, !FHE.eint<2>) -> !FHE.eint<3>
"FHE.sub_int_eint"(%i, %a) : (i3, !FHE.eint<2>) -> !FHE.esint<2>
```

Traits: AlwaysSpeculatableImplTrait

Interfaces: Binary, BinaryIntEint, ConditionallySpeculatable, NoMemoryEffect (MemoryEffectOpInterface)

Effects: MemoryEffects::Effect{}

#### Operands:

| Operand | Description |
| :-----: | ----------- |
| `a` | integer
| `b` | 

#### Results:

| Result | Description |
| :----: | ----------- |
&laquo;unnamed&raquo; | 

### `FHE.to_bool` (::mlir::concretelang::FHE::ToBoolOp)

Cast an unsigned integer to a boolean

The input must be of width one or two. Two being the current representation
of an encrypted boolean, leaving one bit for the carry.

Examples:
```mlir
// ok
"FHE.to_bool"(%x) : (!FHE.eint<1>) -> !FHE.ebool
"FHE.to_bool"(%x) : (!FHE.eint<2>) -> !FHE.ebool

// error
"FHE.to_bool"(%x) : (!FHE.eint<3>) -> !FHE.ebool
```

Traits: AlwaysSpeculatableImplTrait

Interfaces: ConditionallySpeculatable, NoMemoryEffect (MemoryEffectOpInterface), UnaryEint

Effects: MemoryEffects::Effect{}

#### Operands:

| Operand | Description |
| :-----: | ----------- |
| `input` | An encrypted unsigned integer

#### Results:

| Result | Description |
| :----: | ----------- |
&laquo;unnamed&raquo; | An encrypted boolean

### `FHE.to_signed` (::mlir::concretelang::FHE::ToSignedOp)

Cast an unsigned integer to a signed one

The result must have the same width as the input.

The behavior is undefined on overflow/underflow.

Examples:
```mlir
// ok
"FHE.to_signed"(%x) : (!FHE.eint<2>) -> !FHE.esint<2>

// error
"FHE.to_signed"(%x) : (!FHE.eint<2>) -> !FHE.esint<3>
```

Traits: AlwaysSpeculatableImplTrait

Interfaces: ConditionallySpeculatable, NoMemoryEffect (MemoryEffectOpInterface), UnaryEint

Effects: MemoryEffects::Effect{}

#### Operands:

| Operand | Description |
| :-----: | ----------- |
| `input` | An encrypted unsigned integer

#### Results:

| Result | Description |
| :----: | ----------- |
&laquo;unnamed&raquo; | An encrypted signed integer

### `FHE.to_unsigned` (::mlir::concretelang::FHE::ToUnsignedOp)

Cast a signed integer to an unsigned one

The result must have the same width as the input.

The behavior is undefined on overflow/underflow.

Examples:
```mlir
// ok
"FHE.to_unsigned"(%x) : (!FHE.esint<2>) -> !FHE.eint<2>

// error
"FHE.to_unsigned"(%x) : (!FHE.esint<2>) -> !FHE.eint<3>
```

Traits: AlwaysSpeculatableImplTrait

Interfaces: ConditionallySpeculatable, NoMemoryEffect (MemoryEffectOpInterface), UnaryEint

Effects: MemoryEffects::Effect{}

#### Operands:

| Operand | Description |
| :-----: | ----------- |
| `input` | An encrypted signed integer

#### Results:

| Result | Description |
| :----: | ----------- |
&laquo;unnamed&raquo; | An encrypted unsigned integer

### `FHE.zero` (::mlir::concretelang::FHE::ZeroEintOp)

Returns a trivial encrypted integer of 0

Example:
```mlir
"FHE.zero"() : () -> !FHE.eint<2>
"FHE.zero"() : () -> !FHE.esint<2>
```

Traits: AlwaysSpeculatableImplTrait

Interfaces: ConditionallySpeculatable, ConstantNoise, NoMemoryEffect (MemoryEffectOpInterface)

Effects: MemoryEffects::Effect{}

#### Results:

| Result | Description |
| :----: | ----------- |
| `out` | 

### `FHE.zero_tensor` (::mlir::concretelang::FHE::ZeroTensorOp)

Creates a new tensor with all elements initialized to an encrypted zero.

Creates a new tensor with the shape specified in the result type and initializes its elements with an encrypted zero.

Example:
```mlir
%tensor = "FHE.zero_tensor"() : () -> tensor<5x!FHE.eint<4>>
%tensor = "FHE.zero_tensor"() : () -> tensor<5x!FHE.esint<4>>
```

Traits: AlwaysSpeculatableImplTrait

Interfaces: ConditionallySpeculatable, ConstantNoise, NoMemoryEffect (MemoryEffectOpInterface)

Effects: MemoryEffects::Effect{}

#### Results:

| Result | Description |
| :----: | ----------- |
| `tensor` | 

## Type definition

### EncryptedBooleanType

An encrypted boolean

Syntax: `!FHE.ebool`

An encrypted boolean.

### EncryptedSignedIntegerType

An encrypted signed integer

An encrypted signed integer with `width` bits to performs FHE Operations.

Examples:
```mlir
!FHE.esint<7>
!FHE.esint<6>
```

#### Parameters:

| Parameter | C++ type | Description |
| :-------: | :-------: | ----------- |
| width | `unsigned` |  |

### EncryptedUnsignedIntegerType

An encrypted unsigned integer

An encrypted unsigned integer with `width` bits to performs FHE Operations.

Examples:
```mlir
!FHE.eint<7>
!FHE.eint<6>
```

#### Parameters:

| Parameter | C++ type | Description |
| :-------: | :-------: | ----------- |
| width | `unsigned` |  |

