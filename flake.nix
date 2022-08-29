{
  description = "Automation";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/master";
  inputs.flake-utils.url = "github:numtide/flake-utils";

  
  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = nixpkgs.legacyPackages.${system};
    in
    let
    my-python = pkgs.python310;
    automation = my-python.withPackages (p: with p; [
      selenium
    ]);
    in
    {
      devShell = pkgs.mkShell {
        nativeBuildInputs = [ pkgs.bashInteractive ];
        buildInputs = with pkgs; [
        automation
        nodePackages.pyright
        geckodriver
        ];
        shellHook = with pkgs; ''
          PYTHONPATH=${automation}/${automation.sitePackages}
        '';
      };
    });
}
