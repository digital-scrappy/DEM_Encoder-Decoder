with (import <nixpkgs> {
  allowUnfree = true;
});
let
  my-python-packages = python-packages: with python-packages; [
    rasterio
    matplotlib
    notebook
    numpy
    # pytorch-bin
  ];

  python-with-my-packages = python3.withPackages my-python-packages;
in
mkShell {
  buildInputs = [
    python-with-my-packages
  ];
}
