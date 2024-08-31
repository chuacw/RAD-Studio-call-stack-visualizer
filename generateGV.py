import re
import argparse

import GenUtils
from Graph import Graph, quotedGraph
from SysUtils import change_file_ext

# from graphviz import Graph

# Render the graph to a file and view it


# text = "[608EF15E]{vcl290.bpl  } Vcl.Controls.TControl.WndProc (Line 7920, \"Vcl.Controls.pas\" + 91) + $6"
# text2 = "[00B98385]{bds.exe     } AppMain.TAppBuilder.CanCloseProjectGroup + $59"
# Regular expression pattern
pattern = r'\[([0-9a-fA-F]+)\]{(\S+)\s*}\s(\S+)\s*(\([^\)]+\))?(.*)$'

StackEntryRegexStr = pattern
StackEntryRegex = re.compile(StackEntryRegexStr)

def get_safe_name(name):
  return name.replace('.', '_').replace('@', '_').replace('$', '_').replace('%', '_')

# Common procedure for generating a graph
def generate_graph(args, graph_class, node_label_func):
    nodes = {}
    calls = []
    with open(args.callstack) as f:
        lines = f.read().splitlines()

    for idx, line in enumerate(lines):
        regex = StackEntryRegex.match(line)
        if not regex:
            print("ERROR: {}:'{}' does not match regex".format(idx+1, line))
            return
        safe_name = node_label_func(regex.group(3))
        calls.append(safe_name)
        if not safe_name in nodes:
            nodes[safe_name] = regex.group(3)

    calls = reversed(calls)

    g = graph_class("G", "digraph")
    g.node["shape"] = "box"
    prev, curr = None, None
    for idx, call in enumerate(calls):
        prev = curr
        curr = g.add_node("{}".format(call))
        if graph_class == Graph:
            curr["label"] = nodes[call]
        if prev:
            e = g.add_edge(prev, curr)
            e["label"] = "{}".format(idx)

    suffix = ('.verbose' if args.verbose else '.terse') + '.dot'
    output_file = change_file_ext(args.callstack, suffix)
    GenUtils.save_string_to_file(u"" + g.output(), output_file)

    print("File '{}' has been saved".format(output_file))

def processArgs():
  parser = argparse.ArgumentParser()
  parser.add_argument('callstack', type=str, help='Name of file containing call stack')
  # Add an optional argument -v for "verbose"
  parser.add_argument('-v', '--verbose', action='store_true', help='Indicate that the output is verbose')
  
  result = parser.parse_args()

  # Ensure 'callstack' is the first non-optional argument
  if result.callstack is None:
      # Find the first positional argument if not provided
      positional_args = [arg for arg in sys.argv[1:] if not arg.startswith('-')]
      if positional_args:
          result.callstack = positional_args[0]
      else:
          parser.error('No input filename provided')

  return result

def main():
  args = processArgs()
  # if args.verbose: 
  #   generateGV(args)
  # else:
  #   generateQuotedGV(args)
  if args.verbose:
     generate_graph(args, Graph, get_safe_name)
  else:
     generate_graph(args, quotedGraph, lambda name: f'"{name}"')


if __name__ == "__main__":
  main()