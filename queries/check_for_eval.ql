/**
 * @name Check for eval calls
 * @kind problem
 * @problem.severity warning
 * @id python/queries/check_for_eval
 */

import python

predicate isEvalCall(Call c, Name name) {
  c.getFunc() = name and
  name.getId() = "eval"
}

from Call c, Name name
where isEvalCall(c, name) and
  c.getLocation().getFile().getRelativePath().regexpMatch("examples/flask/.*")
select c, "call to 'eval'."
