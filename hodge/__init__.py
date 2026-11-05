"""hodge: small, exact, test-covered computations around the Hodge conjecture.

Modules
-------
griffiths        Hodge numbers of smooth projective hypersurfaces (Griffiths' Jacobian-ring description).
fermat           Hodge characters of Fermat varieties and Shioda's inductive-structure ("decomposability") criterion.
fermat_lines     The 3 m^2 lines on the Fermat surface of degree m, their intersection matrix and its rank.

Everything here is exact integer arithmetic (no floating point), so every number printed by the scripts is a
mathematical statement that can be checked independently.
"""

__all__ = ["griffiths", "fermat", "fermat_lines"]
