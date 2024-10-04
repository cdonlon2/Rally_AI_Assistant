publish:
	rm -rf chase-function.zip
	zip -r chase-function.zip .
	az functionapp deployment source config-zip -g cde-pipeline-test -n cde-pipeline-test-chase-functionapp  --src chase-function.zip --build-remote true