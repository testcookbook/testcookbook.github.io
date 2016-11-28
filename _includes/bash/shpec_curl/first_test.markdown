```text
describe "SHPEC Curl Endpoint Test"
  start="$(date +%s%3N)"
  output="$(curl -s -i 'http://www.testcookbook.com/lib/REST/test.json')"
  end="$(date +%s%3N)"
  runtime=$((end-start))

  it "has runtime less than 1 second"
    assert lt $runtime "1000"
  end

  it "returns a 200 status code"
    assert status_200 "$output"
  end

  it "returns an application/json contentType"
    assert content_type "$output" "application/json"
  end
end
```