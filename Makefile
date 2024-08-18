COSMOS_GOGO_PROTO_URL := https://github.com/cosmos/gogoproto
COSMOS_GOGO_PROTO_VERSION := v1.5.0
COSMOS_GOGO_PROTO_DIR := build/cosmos-gogoproto

COSMOS_SDK_URL := https://github.com/cosmos/cosmos-sdk
COSMOS_SDK_VERSION := v0.50.8
COSMOS_SDK_DIR := build/cosmos-sdk

IBC_GO_URL := https://github.com/cosmos/ibc-go
IBC_GO_VERSION := v8.4.0
IBC_GO_DIR := build/ibc-go

WASMD_URL := https://github.com/cosmwasm/wasmd
WASMD_VERSION := v0.51.0
WASMD_DIR := build/wasmd

XIOND_URL := https://github.com/burnt-labs/xion
XIOND_VERSION := v9.0.0
XIOND_DIR := build/xion

########################################
### Generate protos and grpc files
########################################

proto: fetch_proto_src #buf-deps buf-gen

buf-deps:
	@echo "Updating buf depdendencies..."
	@buf dep update
	@buf dep prune

buf-gen:
	@echo "Generating proto files..."
	@buf build
	@buf generate

fetch_proto_src: $(COSMOS_GOGO_PROTO_DIR) $(COSMOS_SDK_DIR) $(IBC_GO_DIR) $(WASMD_DIR) $(XIOND_DIR)

$(COSMOS_GOGO_PROTO_DIR): Makefile
	rm -rfv $(COSMOS_GOGO_PROTO_DIR)
	git clone --branch $(COSMOS_GOGO_PROTO_VERSION) --depth 1 --quiet --no-checkout --filter=blob:none $(COSMOS_GOGO_PROTO_URL) $(COSMOS_GOGO_PROTO_DIR)
	cd $(COSMOS_GOGO_PROTO_DIR) && git checkout $(COSMOS_GOGO_PROTO_VERSION)

$(COSMOS_SDK_DIR): Makefile
	rm -rfv $(COSMOS_SDK_DIR)
	git clone --branch $(COSMOS_SDK_VERSION) --depth 1 --quiet --no-checkout --filter=blob:none $(COSMOS_SDK_URL) $(COSMOS_SDK_DIR)
	cd $(COSMOS_SDK_DIR) && git checkout $(COSMOS_SDK_VERSION)

$(IBC_GO_DIR): Makefile
	rm -rfv $(IBC_GO_DIR)
	git clone --branch $(IBC_GO_VERSION) --depth 1 --quiet --no-checkout --filter=blob:none $(IBC_GO_URL) $(IBC_GO_DIR)
	cd $(IBC_GO_DIR) && git checkout $(IBC_GO_VERSION)

$(WASMD_DIR): Makefile
	rm -rfv $(WASMD_DIR)
	git clone --branch $(WASMD_VERSION) --depth 1 --quiet --no-checkout --filter=blob:none $(WASMD_URL) $(WASMD_DIR)
	cd $(WASMD_DIR) && git checkout $(WASMD_VERSION)

$(XIOND_DIR): Makefile
	rm -rfv $(XIOND_DIR)
	git clone --branch $(XIOND_VERSION) --depth 1 --quiet --no-checkout --filter=blob:none $(XIOND_URL) $(XIOND_DIR)
	cd $(XIOND_DIR) && git checkout $(XIOND_VERSION)

########################################
### Linting and formatting
########################################

ruff:
	@echo "Running ruff..."
	@ruff check --fix .
