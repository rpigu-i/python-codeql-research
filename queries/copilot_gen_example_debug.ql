/**
 * @name Example Query - checks for DEBUG setting in Django - generated with Copilot
 * @description A simple example query that checks if the Django DEBUG setting is enabled in production code.
 * @kind problem
 * @problem.severity warning
 */

import python

from AssignStmt assign, Name target, BooleanLiteral value
where 
    target = assign.getATarget() and
    target.getId() = "DEBUG" and
    value = assign.getValue() and
    value.booleanValue() = true
select assign, "Django DEBUG setting is enabled in production"
