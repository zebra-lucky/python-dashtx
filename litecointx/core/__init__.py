# Copyright (C) 2018 The python-litecointx developers
#
# This file is part of python-litecointx.
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-litecointx, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE file.

# pylama:ignore=E501

from bitcointx.core import (
    CoreCoinClassDispatcher, CoreCoinClass,

    CTransaction, CTxIn, CTxOut, CTxWitness, CTxInWitness,
    CMutableTransaction, CMutableTxIn, CMutableTxOut, CMutableTxWitness,
    CMutableTxInWitness, COutPoint, CMutableOutPoint
)


class CoreLitecoinClassDispatcher(CoreCoinClassDispatcher):
    ...


class CoreLitecoinClass(CoreCoinClass, metaclass=CoreLitecoinClassDispatcher):
    ...


class CLitecoinOutPoint(COutPoint, CoreLitecoinClass):
    """Litecoin COutPoint"""
    __slots__ = []


class CLitecoinMutableOutPoint(CLitecoinOutPoint, CMutableOutPoint,
                               CoreLitecoinClass, mutable_of=CLitecoinOutPoint):
    """A mutable Litecoin COutPoint"""
    __slots__ = []


class CLitecoinTxIn(CTxIn, CoreLitecoinClass):
    """An immutable Litecoin TxIn"""
    __slots__ = []


class CLitecoinMutableTxIn(CLitecoinTxIn, CMutableTxIn, CoreLitecoinClass,
                           mutable_of=CLitecoinTxIn):
    """A mutable Litecoin TxIn"""
    __slots__ = []


class CLitecoinTxOut(CTxOut, CoreLitecoinClass):
    """A immutable Litecoin TxOut"""
    __slots__ = []


class CLitecoinMutableTxOut(CLitecoinTxOut, CMutableTxOut, CoreLitecoinClass,
                            mutable_of=CLitecoinTxOut):
    """A mutable Litecoin CTxOut"""
    __slots__ = []


class CLitecoinTxInWitness(CTxInWitness, CoreLitecoinClass):
    """Immutable Litecoin witness data for a single transaction input"""
    __slots__ = []


class CLitecoinMutableTxInWitness(CLitecoinTxInWitness, CMutableTxInWitness,
                                  CoreLitecoinClass,
                                  mutable_of=CLitecoinTxInWitness):
    """Mutable Litecoin witness data for a single transaction input"""
    __slots__ = []


class CLitecoinTxWitness(CTxWitness, CoreLitecoinClass):
    """Immutable witness data for all inputs to a transaction"""
    __slots__ = []


class CLitecoinMutableTxWitness(CLitecoinTxWitness, CMutableTxWitness,
                                CoreLitecoinClass,
                                mutable_of=CLitecoinTxWitness):
    """Witness data for all inputs to a transaction, mutable version"""
    __slots__ = []


class CLitecoinTransaction(CTransaction, CoreLitecoinClass):
    """Litecoin transaction, mutable version"""
    __slots__ = []


class CLitecoinMutableTransaction(CLitecoinTransaction, CMutableTransaction,
                                  CoreLitecoinClass,
                                  mutable_of=CLitecoinTransaction):
    """Litecoin transaction"""
    __slots__ = []


__all__ = (
    'CLitecoinOutPoint',
    'CLitecoinMutableOutPoint',
    'CLitecoinTxIn',
    'CLitecoinMutableTxIn',
    'CLitecoinTxOut',
    'CLitecoinMutableTxOut',
    'CLitecoinTransaction',
    'CLitecoinMutableTransaction',
    'CLitecoinTxWitness',
    'CLitecoinMutableTxWitness',
    'CLitecoinMutableTxInWitness',
    'CLitecoinTxInWitness',
)
