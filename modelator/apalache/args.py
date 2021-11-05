from recordclass import recordclass

apalache_args_fields = (
    "cmd",  # The Apalache <command> to run. (check | config | parse | test | typecheck | noop)
    "file",  # A file containing a TLA+ specification (.tla or .json)
    "debug",  # extensive logging in detailed.log and log.smt, default: false
    "out_dir",  # where output files will be written, default: ./_apalache-out (overrides envvar OUT_DIR) (relative to cwd)
    "profiling",  # write general profiling data to profile-rules.txt in the run directory, default: false (overrides envvar PROFILING)
    "smtprof",  # profile SMT constraints in log.smt, default: false
    "write_intermediate",  # write intermediate output files to `out-dir`, default: false (overrides envvar WRITE_INTERMEDIATE)
    "algo",  # the search algorithm: offline, incremental, parallel (soon), default: incremental
    "cinit",  # the name of an operator that initializes CONSTANTS, default: None
    "config",  # configuration file in TLC format, default: <file>.cfg, or none if <file>.cfg not present
    "discard_disabled",  # pre-check, whether a transition is disabled, and discard it, to make SMT queries smaller, default: true
    "init",  # the name of an operator that initializes VARIABLES, default: Init
    "inv",  # the name of an invariant operator, e.g., Inv
    "length",  # maximal number of Next steps, default: 10
    "max_error",  # do not stop on first error, but produce up to a given number of counterexamples (fine tune with --view), default: 1
    "next",  # the name of a transition operator, default: Next
    "no_deadlock",  # do not check for deadlocks, default: true
    "nworkers",  # the number of workers for the parallel checker (soon), default: 1
    "smt_encoding",  # the SMT encoding: oopsla19, arrays (experimental), default: oopsla19 (overrides envvar SMT_ENCODING)
    "tuning",  # filename of the tuning options, see docs/tuning.md
    "tuning_options",  # tuning options as arguments in the format key1=val1:key2=val2:key3=val3 (priority over --tuning)
    "view",  # the state view to use with --max-error=n, default: transition index
    "enable_stats",  # Let Apalache submit usage statistics to tlapl.us (shared with TLC and TLA+ Toolbox). See: https://apalache.informal.systems/docs/apalache/statistics.html
    "output",  # filename where to output the parsed source (.tla or .json), default: None
    "before",  # the name of an operator to prepare the test, similar to Init
    "action",  # the name of an action to execute, similar to Next
    "assertion",  # the name of an operator that should evaluate to true after executing `action`
    "infer_poly",  # allow the type checker to infer polymorphic types, default: true
)

ApalacheArgs = recordclass(
    "ApalacheArgs", apalache_args_fields, defaults=(None,) * len(apalache_args_fields)
)

"""
# APALACHE version 0.17.0 build f62f370
#
# WARNING: This tool is in the experimental stage.
#          Please report bugs at: [https://github.com/informalsystems/apalache/issues]
#
# Usage statistics is ON. Thank you!
# If you have changed your mind, disable the statistics with config --enable-stats=false.

Usage

 apalache-mc [options] command [command options]

Options

   --debug              : extensive logging in detailed.log and log.smt, default: false
   --out-dir            : where output files will be written, default: ./_apalache-out (overrides envvar OUT_DIR)
   --profiling          : write general profiling data to profile-rules.txt in the run directory, default: false (overrides envvar PROFILING)
   --smtprof            : profile SMT constraints in log.smt, default: false
   --write-intermediate : write intermediate output files to `out-dir`, default: false (overrides envvar WRITE_INTERMEDIATE)

Commands

   check [command options] <file> : Check a TLA+ specification
      --algo=STRING           : the search algorithm: offline, incremental, parallel (soon), default: incremental
      --cinit=STRING          : the name of an operator that initializes CONSTANTS,
                                default: None
      --config=STRING         : configuration file in TLC format,
                                default: <file>.cfg, or none if <file>.cfg not present
      --discard-disabled      : pre-check, whether a transition is disabled, and discard it, to make SMT queries smaller, default: true
      --init=STRING           : the name of an operator that initializes VARIABLES,
                                default: Init
      --inv=STRING            : the name of an invariant operator, e.g., Inv
      --length=NUM            : maximal number of Next steps, default: 10
      --max-error=NUM         : do not stop on first error, but produce up to a given number of counterexamples (fine tune with --view), default: 1
      --next=STRING           : the name of a transition operator, default: Next
      --no-deadlock           : do not check for deadlocks, default: true
      --nworkers=NUM          : the number of workers for the parallel checker (soon), default: 1
      --smt-encoding          : the SMT encoding: oopsla19, arrays (experimental), default: oopsla19 (overrides envvar SMT_ENCODING)
      --tuning=STRING         : filename of the tuning options, see docs/tuning.md
      --tuning-options=STRING : tuning options as arguments in the format key1=val1:key2=val2:key3=val3 (priority over --tuning)
      --view=STRING           : the state view to use with --max-error=n, default: transition index
      <file> : a file containing a TLA+ specification (.tla or .json)

   config [command options] : Configure Apalache options
      --enable-stats : Let Apalache submit usage statistics to tlapl.us
                       (shared with TLC and TLA+ Toolbox)
                       See: https://apalache.informal.systems/docs/apalache/statistics.html

   parse [command options] <file> : Parse a TLA+ specification and quit
      --output=STRING : filename where to output the parsed source (.tla or .json),
                        default: None
      <file> : a file containing a TLA+ specification (.tla or .json)

   test [command options] <file> <before> <action> <assertion> : Quickly test a TLA+ specification
      --cinit=STRING : the name of an operator that initializes CONSTANTS,
                       default: None
      <file>    : a file containing a TLA+ specification (.tla or .json)
      <before>  : the name of an operator to prepare the test, similar to Init
      <action>  : the name of an action to execute, similar to Next
      <assertion> : the name of an operator that should evaluate to true after executing `action`

   typecheck [command options] <file> : Check types in a TLA+ specification
      --infer-poly : allow the type checker to infer polymorphic types, default: true
      <file> : a TLA+ specification (.tla or .json)

No command found, expected one of check, config, parse, test, typecheck

"""
