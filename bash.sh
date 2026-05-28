args=()
for file in allure-results/*; do
  if [ -f "$file" ]; then
    args+=(-F "files[]=@$file")
  fi
done
curl -X POST "http://127.0.0.1:5050/allure-docker-service/send-results?project_id=default" "${args[@]}"