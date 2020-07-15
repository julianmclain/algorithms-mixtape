# Topological Sort

A topological ordering of a directed graph *G* is a labelling function *f* of
*G*'s nodes such that:
1. Every node receives a sequential value, for example the set of positive
   integers starting at 1.
2. For every edge, the *f* value of the tail must be less than the *f* value of
   the head. (*u*, *v*) ε *G* => *f*(*u*) < *f*(*v*)

Topological orderings can be used to sequence tasks while respecting all
precedence constraints. For example, a topological ordering can sequence the
courses required to complete an undergraduate degree.

Topological orderings are always present in acyclic directed graphs (there can
be more than one). If the graph *G* has a directed cycle, there is not
topological ordering.

## Asymptotic runtime

The runtime is linear *O*(*n* + *m*).