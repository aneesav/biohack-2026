#!/usr/bin/env python3
"""Annotate mitochondrial genes and compute scRNA-seq QC metrics on an AnnData file.

A minimal, scriptable version of the QC step in notebooks/01_data_ingest_and_qc.ipynb --
useful once you've picked thresholds interactively and want to apply them in a
reproducible pipeline step instead of a notebook.
"""
import argparse

import scanpy as sc


def main(input_file: str, output_file: str) -> None:
    adata = sc.read_h5ad(input_file)
    adata.var["mt"] = adata.var_names.str.startswith("MT-")

    sc.pp.calculate_qc_metrics(
        adata,
        qc_vars=["mt"],
        percent_top=None,
        log1p=False,
        inplace=True,
    )

    adata.write(output_file)
    print(f"QC metrics added. Output saved to: {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Annotate MT genes & compute QC metrics on an AnnData .h5ad file"
    )
    parser.add_argument("input", help="Path to input AnnData .h5ad file")
    parser.add_argument("output", help="Path to output AnnData .h5ad file")
    args = parser.parse_args()
    main(args.input, args.output)
