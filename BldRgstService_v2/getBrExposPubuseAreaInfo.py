"""
건축물대장 건물층별 정보 api test
"""

# 요청 파라메터 명세
"""
bjdongCd    법정동코드   VARCHAR2(5) 필   10300   행정표준코드
platGbCd    대지구분코드  CHAR(1) 옵   0   0:대지 1:산 2:블록
bun 번   VARCHAR2(4) 옵   0012    번
ji  지   VARCHAR2(4) 옵   0000    지
startDate   검색시작일   VARCHAR2(8) 옵       YYYYMMDD
endDate 검색종료일   VARCHAR2(8) 옵       YYYYMMDD
numOfRows   리스트수    VARCHAR2(3) 옵   10  페이지당 목록 수
pageNo  페이지번호   VARCHAR2(3) 옵   1   페이지번호
sigunguCd   시군구코드   VARCHAR2(5) 필   11680   행정표준코드
"""
# 필수 파라메터
"""
    sigunguCd=11170  # 시군구코드
    bjdongCd=12500  # 법정동코드
    bun=0424  # 번지 (API상 필수는 아니지만 건축물 특정에 필요)
    platGbCd=0  # 대지구분코드 (안넣으니 건물 데이터 안나옴)
"""

import requests
import xml.etree.ElementTree as ET

_api_secret_key = "2YuPAXqZChXC6W43vzUXOMNLuuYmV8naX2yLIO91DJgoVKeIaTUw2cI%2F%2F5Nh13w9CQU%2FcFDZkTQBr7tRY6U0zA%3D%3D"
_api_decode_ke = "2YuPAXqZChXC6W43vzUXOMNLuuYmV8naX2yLIO91DJgoVKeIaTUw2cI//5Nh13w9CQU/cFDZkTQBr7tRY6U0zA=="


def format_building_info(response):
    building_info = []

    # XML 파싱
    xml_data = response.content
    root = ET.fromstring(xml_data)

    # items 아래의 각 item을 순회하며 데이터 추출 예제
    # item 요소들을 찾아서 데이터 추출
    items = root.find('body/items')
    if items is not None:
        for item in items.findall('item'):
            area = item.findtext('area')
            bldNm = item.findtext('bldNm')
            bun = item.findtext('bun')
            crtnDay = item.findtext('crtnDay')
            etcPurps = item.findtext('etcPurps')
            flrNoNm = item.findtext('flrNoNm')
            mainPurpsCdNm = item.findtext('mainPurpsCdNm')
            mgmBldrgstPk = item.findtext('mgmBldrgstPk')
            platPlc = item.findtext('platPlc')

            # 데이터 처리 예시: 딕셔너리 형태로 저장
            item_data = {
                'area': area,
                'bldNm': bldNm,
                'bun': bun,
                'crtnDay': crtnDay,
                'etcPurps': etcPurps,
                'flrNoNm': flrNoNm,
                'mainPurpsCdNm': mainPurpsCdNm,
                'mgmBldrgstPk': mgmBldrgstPk,
                'platPlc': platPlc
            }

            # 리스트에 딕셔너리 추가
            building_info.append(item_data)

            # 딕셔너리를 리스트에 추가
            # 이 부분에서 필요에 따라 리스트에 추가하거나, 데이터를 가공할 수 있습니다.
            # 예를 들어, 여기서는 그냥 출력하는 예시를 드리겠습니다.
            print(f'건물명: {bldNm}, 층수: {flrNoNm}, 면적: {area}, 용도: {mainPurpsCdNm}, 관리번호: {mgmBldrgstPk}')

        return building_info


def main():
    request_url = 'https://apis.data.go.kr/1613000/BldRgstService_v2/getBrExposPubuseAreaInfo'
    sigunguCd = "11170"
    bjdongCd = "12500"
    bun = "0424"
    platGbCd = "0"

    query_params = {
        'serviceKey': _api_decode_ke,
        'sigunguCd': sigunguCd,
        'bjdongCd': bjdongCd,
        'bun': bun,
        'platGbCd': platGbCd,
        'numOfRows': "100"
    }

    response = requests.get(request_url, params=query_params)
    # print(response.text)
    building_info = format_building_info(response)

    return 0


if __name__ == '__main__':
    main()
