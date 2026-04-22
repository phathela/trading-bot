import json
from app import app

def test_3commas_webhook():
    """Test 3Commas webhook conversion"""
    print("\n" + "=" * 60)
    print("3COMMAS WEBHOOK CONVERSION TESTS")
    print("=" * 60)

    with app.test_client() as client:
        # Test 1: enter_long (should trigger Buy)
        print("\n1. Testing enter_long (Buy signal)")
        print("-" * 40)
        payload = {
            "secret": "eyJhbGciOiJIUzI1NiJ9.eyJzaWduYWxzX3NvdXJjZV9pZCI6NTc4Mzl9.F2p3voUTipO8hY-JqZezt0qJyEX9lr6JQqr-zc1fbyw",
            "max_lag": "300",
            "timestamp": "2026-04-22T20:00:00",
            "trigger_price": "45000",
            "tv_exchange": "BINANCE",
            "tv_instrument": "BTCUSDT",
            "action": "enter_long",
            "bot_uuid": "d97dabb2-b1c3-4596-baa1-ae8c5f23ebb6"
        }
        response = client.post('/webhook/3commas',
            data=json.dumps(payload),
            content_type='application/json')
        print(f"Status: {response.status_code}")
        data = response.get_json()
        print(f"Signal: {data['signal']}")
        print(f"Indicator A: {data['indicator_signals']['indicator_a']}")
        print(f"Indicator B: {data['indicator_signals']['indicator_b']}")
        assert response.status_code == 200
        assert data['signal'] == 'Buy'
        print("PASS")

        # Test 2: enter_short (should trigger Sell)
        print("\n2. Testing enter_short (Sell signal)")
        print("-" * 40)
        payload['action'] = 'enter_short'
        response = client.post('/webhook/3commas',
            data=json.dumps(payload),
            content_type='application/json')
        print(f"Status: {response.status_code}")
        data = response.get_json()
        print(f"Signal: {data['signal']}")
        assert response.status_code == 200
        assert data['signal'] == 'Sell'
        print("PASS")

        # Test 3: close_long (should trigger Sell)
        print("\n3. Testing close_long (Sell signal)")
        print("-" * 40)
        payload['action'] = 'close_long'
        response = client.post('/webhook/3commas',
            data=json.dumps(payload),
            content_type='application/json')
        print(f"Status: {response.status_code}")
        data = response.get_json()
        print(f"Signal: {data['signal']}")
        assert response.status_code == 200
        assert data['signal'] == 'Sell'
        print("PASS")

        # Test 4: close_short (should trigger Buy)
        print("\n4. Testing close_short (Buy signal)")
        print("-" * 40)
        payload['action'] = 'close_short'
        response = client.post('/webhook/3commas',
            data=json.dumps(payload),
            content_type='application/json')
        print(f"Status: {response.status_code}")
        data = response.get_json()
        print(f"Signal: {data['signal']}")
        assert response.status_code == 200
        assert data['signal'] == 'Buy'
        print("PASS")

        # Test 5: Invalid action
        print("\n5. Testing invalid action (should return 400)")
        print("-" * 40)
        payload['action'] = 'invalid_action'
        response = client.post('/webhook/3commas',
            data=json.dumps(payload),
            content_type='application/json')
        print(f"Status: {response.status_code}")
        assert response.status_code == 400
        print("PASS - Correctly rejected invalid action")

    print("\n" + "=" * 60)
    print("ALL 3COMMAS TESTS PASSED!")
    print("=" * 60)
    print("\n3Commas webhook conversion is working correctly")
    print("Ready to change webhook URL in TradingView")

if __name__ == '__main__':
    test_3commas_webhook()
