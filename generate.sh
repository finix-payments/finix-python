find ./finix/model ! -name 'finix_utils.py' -type f -exec rm -f {} +

openapi-generator generate \
  -g python \
  -t template \
  -i spec/finix_openapi.yaml \
  -o ${PWD} \
  --skip-validate-spec \
  --global-property skipFormModel=false \
  --reserved-words-mappings self=self \
  --additional-properties=packageName=finix \
  --additional-properties=packageVersion=4.0.0 \
  --additional-properties=projectName=finix \
  --global-property apiDocs=false \
  --global-property modelDocs=false \
  --global-property apiTests=false \
  --global-property modelTests=false 
  
  rm -rf .openapi-generator