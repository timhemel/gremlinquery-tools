# Testing Gremlin queries

Gremtest is a joshi script that lets you test Gremlin queries against an Octopus server.

# Usage

To create a test script, include gremtest:

  #include gremtest.grm

Then, define your tests, giving it a test name, a closure containing the test code, and an optional flag to enable or disable the test. For example:

```
test( "function name traversal", { ->
	fname = g.V()
		.has(NODE_TYPE,TYPE_FUNCTION)
		.has(NODE_CODE,'tut3')
		.values('code')
		.next()
	assertEquals( fname, 'tut3')
})
```

At the end, call `run_tests`:

  run_tests()

# Output

The script will return a list of test results, all formatted for terminal output. For example:

```
function name traversal            : PASS
test with error                    : ERROR
Division by zero
at Script7$_run_closure2(doCall:80)
at Script7(do_test:16)
at Script7$do_test$0(callCurrent:-1)
at Script7$do_test$0(callCurrent:-1)
at Script7(test:40)
at Script7(test:-1)
at Script7$test(callCurrent:-1)
at Script7(run:79)
at octopus.server.gremlinShell.OctopusGremlinShell(execute:122)
at octopus.server.gremlinShell.ShellRunnable(evaluteOnShell:145)
at octopus.server.gremlinShell.ShellRunnable(handleClient:136)
at octopus.server.gremlinShell.ShellRunnable(processClients:69)
at octopus.server.gremlinShell.ShellRunnable(run:44)

failing test                       : FAIL
assert expected == found
       |        |  |
       1        |  2
                false
1 pass, 1 fail, 1 error(s)
```

The texts `PASS`, `ERROR` and `FAIL` are color coded to immediately see the results at a glance.

