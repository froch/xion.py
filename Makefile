COSMOS_SDK_URL := https://github.com/cosmos/cosmos-sdk
COSMOS_SDK_VERSION := v0.50.8
COSMOS_SDK_DIR := build/cosmos-sdk

XIOND_URL := https://github.com/burnt-labs/xion
XIOND_VERSION := v9.0.0
XIOND_DIR := build/xion

########################################
### Generate protos and grpc files
########################################

proto: fetch_proto_schema_source buf-deps buf-gen

fetch_proto_schema_source: $(COSMOS_SDK_DIR) $(XIOND_DIR)

$(COSMOS_SDK_DIR): Makefile
	rm -rfv $(COSMOS_SDK_DIR)
	git clone --branch $(COSMOS_SDK_VERSION) --depth 1 --quiet --no-checkout --filter=blob:none $(COSMOS_SDK_URL) $(COSMOS_SDK_DIR)
	cd $(COSMOS_SDK_DIR) && git checkout $(COSMOS_SDK_VERSION)

$(XIOND_DIR): Makefile
	rm -rfv $(XIOND_DIR)
	git clone --branch $(XIOND_VERSION) --depth 1 --quiet --no-checkout --filter=blob:none $(XIOND_URL) $(XIOND_DIR)
	cd $(XIOND_DIR) && git checkout $(XIOND_VERSION)

buf-deps:
	@echo "Updating buf depdendencies..."
	@buf dep update
	@buf dep prune

buf-gen:
	@echo "Generating proto files..."
	@buf build
	@buf generate
