$date = Get-Date -format "yyyyMMdd"
$UploadPath = "<upload path>"
cd $UploadPath
Get-ChildItem $UploadPath | 
Foreach-Object {
	$UpdatedFileName = $_.BaseName + "-" + $date + $_.Extension
	aws s3 cp $_.FullName <S3 URI>/$UpdatedFileName
	if($?){
		Remove-Item -Path $_.FullName
	}else{
		exit $LASTEXITCODE
	}	
}

