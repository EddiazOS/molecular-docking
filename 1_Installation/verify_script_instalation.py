import subprocess
import sys

print("==== Verificación del Ambiente de Docking ====\n")

# Verificar Vina
result = subprocess.run(["vina", "--version"], capture_output=True, text=True)
print(f"AutoDock Vina: {result.stdout.strip() or result.stderr.strip()}")

# Verificar Babel
result = subprocess.run(["obabel", "-V"], capture_output=True, text=True)
print(f"Open Babel: {result.stdout.strip() or result.stderr.strip()}")

# Verificar Python
print(f"Python: {sys.version}")

# Verificar librerías
libreries = ["numpy", "meeko"]
for lib in libreries:
    try:
        __import__(lib)
        import importlib.metadata
        version = importlib.metadata.version(lib)
        print(f"{lib}: (v{version})")
    except Exception as e:
        print(f"{lib}: ERROR - {e}")

print("\n=== Verificación completa ===")