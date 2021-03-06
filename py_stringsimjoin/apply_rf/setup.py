from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(ext_modules = cythonize([
    Extension("tokenizers", sources=["tokenizers.pyx"], language="c++",
              extra_compile_args = ["-O3", "-ffast-math", "-march=native", "-fopenmp"],
              extra_link_args=['-fopenmp']),
    Extension("sim_functions", sources=["sim_functions.pyx"], language="c++",         
              extra_compile_args = ["-O3", "-ffast-math", "-march=native"]),  
    Extension("set_sim_join", sources=["set_sim_join.pyx", "cache.cpp", "position_index.cpp"], language="c++",             
              extra_compile_args = ["-O3", "-ffast-math", "-march=native", "-fopenmp"], 
              extra_link_args=['-fopenmp']),
    Extension("overlap_coefficient_join", sources=["overlap_coefficient_join.pyx", "cache.cpp", "inverted_index.cpp"], language="c++",
              extra_compile_args = ["-O3", "-ffast-math", "-march=native", "-fopenmp"],
              extra_link_args=['-fopenmp']),
    Extension("edit_distance_join", sources=["edit_distance_join.pyx", "inverted_index.cpp"], language="c++",
              extra_compile_args = ["-O3", "-ffast-math", "-march=native", "-fopenmp"],
              extra_link_args=['-fopenmp']),  
    Extension("executor", sources=["executor.pyx", "cache.cpp", "node.cpp", "predicatecpp.cpp", "tree.cpp","rule.cpp","coverage.cpp"], language="c++",         
              extra_compile_args = ["-O3", "-ffast-math", "-march=native", "-fopenmp"],
              extra_link_args=['-fopenmp']),
    Extension("ex_plan", sources=["ex_plan.pyx", "tree.cpp", "rule.cpp", "predicatecpp.cpp", "coverage.cpp", "node.cpp"], language="c++",
              extra_compile_args = ["-O3", "-ffast-math", "-march=native", "-fopenmp"],
              extra_link_args=['-fopenmp']),
    Extension("utils", sources=["utils.pyx", "inverted_index.cpp"], language="c++",
              extra_compile_args = ["-O3", "-ffast-math", "-march=native", "-fopenmp"],
              extra_link_args=['-fopenmp']),
    Extension("sample", sources=["sample.pyx", "inverted_index.cpp"], language="c++",
              extra_compile_args = ["-O3", "-ffast-math", "-march=native", "-fopenmp"],
              extra_link_args=['-fopenmp']),
    Extension("execute_join_node", sources=["execute_join_node.pyx", "predicatecpp.cpp"], language="c++",         
              extra_compile_args = ["-O3", "-ffast-math", "-march=native", "-fopenmp"],
              extra_link_args=['-fopenmp']),
    Extension("execute_feature_node", sources=["execute_feature_node.pyx", "predicatecpp.cpp"], language="c++",
              extra_compile_args = ["-O3", "-ffast-math", "-march=native", "-fopenmp"],
              extra_link_args=['-fopenmp']),
    Extension("execute_filter_node", sources=["execute_filter_node.pyx", "predicatecpp.cpp"], language="c++",
              extra_compile_args = ["-O3", "-ffast-math", "-march=native", "-fopenmp"],
              extra_link_args=['-fopenmp']),
    Extension("execute_select_node", sources=["execute_select_node.pyx", "predicatecpp.cpp"], language="c++",
              extra_compile_args = ["-O3", "-ffast-math", "-march=native", "-fopenmp"],
              extra_link_args=['-fopenmp']), 
 ]))
