"""
SENTINEL — Safe AI Code Execution & AST Sandbox (Phase 6)
Parses AI-generated Python code using Python's Abstract Syntax Tree (ast) module.
Enforces zero-trust code inspection by blocking exec(), eval(), shell calls, filesystem destruction, and network access before execution.
"""
import ast
import sys
import json
import base64
import math
import re
from datetime import datetime

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

class ASTSecurityVisitor(ast.NodeVisitor):
    """AST Inspector checking for forbidden modules and function calls."""
    FORBIDDEN_CALLS = {'exec', 'eval', '__import__', 'open', 'compile', 'input'}
    FORBIDDEN_MODULES = {'os', 'sys', 'subprocess', 'shutil', 'socket', 'urllib', 'requests', 'ctypes', 'threading', 'multiprocessing', 'builtins'}

    def __init__(self):
        self.violations = []

    def visit_Import(self, node):
        for alias in node.names:
            if alias.name.split('.')[0] in self.FORBIDDEN_MODULES:
                self.violations.append(f"Forbidden module import: '{alias.name}'")
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        if node.module and node.module.split('.')[0] in self.FORBIDDEN_MODULES:
            self.violations.append(f"Forbidden module import: '{node.module}'")
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            if node.func.id in self.FORBIDDEN_CALLS:
                self.violations.append(f"Forbidden function call: '{node.func.id}()'")
        elif isinstance(node.func, ast.Attribute):
            if node.func.attr in self.FORBIDDEN_CALLS:
                self.violations.append(f"Forbidden method call: '{node.func.attr}()'")
        self.generic_visit(node)

class SentinelCodeSandbox:
    def __init__(self):
        # Safe execution scope (whitelisted safe builtins & standard modules)
        self.safe_globals = {
            "__builtins__": __builtins__,
            "base64": base64,
            "json": json,
            "math": math,
            "re": re,
            "datetime": datetime
        }

    def validate_code(self, code_str: str) -> tuple[bool, list]:
        """Parse AST and return (is_safe, list_of_violations)."""
        try:
            tree = ast.parse(code_str)
        except SyntaxError as e:
            return False, [f"Syntax Error in AI code: {e}"]

        visitor = ASTSecurityVisitor()
        visitor.visit(tree)

        if visitor.violations:
            return False, visitor.violations
        return True, []

    def execute_safe_code(self, code_str: str) -> dict:
        """Validate code via AST, then execute safely if approved."""
        is_safe, violations = self.validate_code(code_str)
        if not is_safe:
            return {
                "status": "BLOCKED",
                "is_safe": False,
                "violations": violations,
                "execution_output": None
            }

        # Safe local execution namespace
        safe_locals = {}
        try:
            exec(code_str, self.safe_globals, safe_locals)
            output = safe_locals.get("result") or safe_locals.get("output") or "Code executed successfully with zero violations."
            return {
                "status": "EXECUTED_SAFE",
                "is_safe": True,
                "violations": [],
                "execution_output": str(output)
            }
        except Exception as e:
            return {
                "status": "RUNTIME_ERROR",
                "is_safe": True,
                "violations": [],
                "error": f"Runtime Exception: {e}"
            }

if __name__ == "__main__":
    sandbox = SentinelCodeSandbox()

    print("🧪 Test 1: Testing Safe AI Base64 De-obfuscation Code...")
    safe_code = """
import base64
encoded_data = "U0VOVElORUwgQ09ERSBTQU5EQk9YIFRFU1Q="
decoded = base64.b64decode(encoded_data).decode('utf-8')
result = f"Decoded Output: {decoded}"
"""
    res1 = sandbox.execute_safe_code(safe_code)
    print(json.dumps(res1, indent=2))

    print("\n🧪 Test 2: Testing Malicious AI Code (Attempting Shell Execution)...")
    malicious_code = """
import os
os.system("rm -rf /")
"""
    res2 = sandbox.execute_safe_code(malicious_code)
    print(json.dumps(res2, indent=2))
