# DAFNI Model Uploader action

This action takes your Model Definition file and compressed Docker image file and
uploads them to DAFNI as a new Model version.

## Inputs

### `definition-path`

**Required** The path to your Model Definition file.

### `image-path`

**Required** The path to your Model's compressed Docker image file.

### `username`

**Required** Your DAFNI username.

### `password`

**Required** Your DAFNI password.

### `version-message`

**Required** A version message to use for your Model version. Default `"Uploaded from DAFNI Model Uploader"`.

### `parent-model`

The ID of the parent Model on DAFNI you want to associate the new version with. Optional - if not specified a new Model will be created on DAFNI.

## Example usage

uses: actions/dafni-model-uploader@v1
with:
  definition-path: 'path/to/model_definition.yaml'
  image-path: 'path/to/image.tar.gz'
  username: 'dafni-username'
  password: 'password123!'
  version-message: 'I'm uploading my Model automatically!'
  parent-model: '62774935-f7d3-40b0-aa69-7faac8c800c7'