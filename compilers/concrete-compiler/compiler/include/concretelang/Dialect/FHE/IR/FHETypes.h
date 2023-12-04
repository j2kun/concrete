// Part of the Concrete Compiler Project, under the BSD3 License with Zama
// Exceptions. See
// https://github.com/zama-ai/concrete-compiler-internal/blob/main/LICENSE.txt
// for license information.

#ifndef CONCRETELANG_DIALECT_FHE_IR_FHETYPES_H
#define CONCRETELANG_DIALECT_FHE_IR_FHETYPES_H

#include "llvm/ADT/TypeSwitch.h"
#include <mlir/IR/BuiltinOps.h>
#include <mlir/IR/BuiltinTypes.h>
#include <mlir/IR/DialectImplementation.h>

#include <mlir/Dialect/Arith/IR/Arith.h>

#include "concretelang/Dialect/FHE/Interfaces/FHEInterfaces.h"

#define GET_TYPEDEF_CLASSES
#include "concretelang/Dialect/FHE/IR/FHEOpsTypes.h.inc"

#endif
