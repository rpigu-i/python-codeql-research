/**
 * @name Django Avoid execute_from_command_line
 * @kind problem
 * @problem.severity warning
 * @id python/queries/execute_from_command_line
 */

import python


from Call c, Name name 
where name.getId() = "execute_from_command_line" and
c.getFunc() = name and 
c.getLocation().getFile().getRelativePath().regexpMatch("examples/django/.*")
select c, "Avoid using execute_from_command_line in Django examples."
