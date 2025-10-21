/**
 * @name Check for exec calls
 * @kind problem
 * @problem.severity warning
 * @id python/example/check_for_exec
 */

import python

class ExecCall extends Call {
  ExecCall() {
    exists(Name name |
      this.getFunc() = name |
      name.getId() = "exec")
  }
}

from Call c
where c instanceof ExecCall and
  c.getLocation().getFile().getRelativePath().regexpMatch("examples/flask/.*")
select c, "call to 'exec'."
