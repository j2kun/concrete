// Part of the Concrete Compiler Project, under the BSD3 License with Zama
// Exceptions. See
// https://github.com/zama-ai/concrete-compiler-internal/blob/main/LICENSE.txt
// for license information.

#ifndef CONCRETELANG_DIALECT_TFHE_IR_TFHEATTRS_H
#define CONCRETELANG_DIALECT_TFHE_IR_TFHEATTRS_H

#include "concretelang/Dialect/TFHE/IR/TFHEParameters.h"
#include "llvm/ADT/TypeSwitch.h"
#include <mlir/Dialect/Func/IR/FuncOps.h>
#include <mlir/IR/BuiltinOps.h>
#include <mlir/IR/BuiltinTypes.h>
#include <mlir/IR/DialectImplementation.h>

#define GET_ATTRDEF_CLASSES
#include "concretelang/Dialect/TFHE/IR/TFHEAttrs.h.inc"

#endif
