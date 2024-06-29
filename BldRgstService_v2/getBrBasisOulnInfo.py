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
_api_decode_key = "2YuPAXqZChXC6W43vzUXOMNLuuYmV8naX2yLIO91DJgoVKeIaTUw2cI//5Nh13w9CQU/cFDZkTQBr7tRY6U0zA=="

def format_building_info(response):

    building_info = []

    # XML 파싱
    xml_data = response.content
    root = ET.fromstring(xml_data)

    data_list = []

    items = root.find('body/items')
    # print(f"items:{items.text}")

    if items is not None:
        for item in items.findall('item'):
            data = {
                'archArea': item.findtext('archArea'),
                'atchBldArea': item.findtext('atchBldArea'),
                'atchBldCnt': item.findtext('atchBldCnt'),
                'bcRat': item.findtext('bcRat'),
                'bjdongCd': item.findtext('bjdongCd'),
                'bldNm': item.findtext('bldNm'),
                'block': item.findtext('block'),
                'bun': item.findtext('bun'),
                'bylotCnt': item.findtext('bylotCnt'),
                'crtnDay': item.findtext('crtnDay'),
                'dongNm': item.findtext('dongNm'),
                'emgenUseElvtCnt': item.findtext('emgenUseElvtCnt'),
                'engrEpi': item.findtext('engrEpi'),
                'engrGrade': item.findtext('engrGrade'),
                'engrRat': item.findtext('engrRat'),
                'etcPurps': item.findtext('etcPurps'),
                'etcRoof': item.findtext('etcRoof'),
                'etcStrct': item.findtext('etcStrct'),
                'fmlyCnt': item.findtext('fmlyCnt'),
                'gnBldCert': item.findtext('gnBldCert'),
                'gnBldGrade': item.findtext('gnBldGrade'),
                'grndFlrCnt': item.findtext('grndFlrCnt'),
                'heit': item.findtext('heit'),
                'hhldCnt': item.findtext('hhldCnt'),
                'hoCnt': item.findtext('hoCnt'),
                'indrAutoArea': item.findtext('indrAutoArea'),
                'indrAutoUtcnt': item.findtext('indrAutoUtcnt'),
                'indrMechArea': item.findtext('indrMechArea'),
                'indrMechUtcnt': item.findtext('indrMechUtcnt'),
                'itgBldCert': item.findtext('itgBldCert'),
                'itgBldGrade': item.findtext('itgBldGrade'),
                'ji': item.findtext('ji'),
                'lot': item.findtext('lot'),
                'mainAtchGbCd': item.findtext('mainAtchGbCd'),
                'mainAtchGbCdNm': item.findtext('mainAtchGbCdNm'),
                'mainPurpsCd': item.findtext('mainPurpsCd'),
                'mainPurpsCdNm': item.findtext('mainPurpsCdNm')
            }

            # 리스트에 딕셔너리 추가
            building_info.append(data)

    # print(f'building_info: {building_info}')

    return building_info


def main():

    request_url = 'https://apis.data.go.kr/1613000/BldRgstService_v2/getBrBasisOulnInfo'
    sigunguCd= "11170"
    bjdongCd= "12500"
    bun= "0424"
    platGbCd = "0"

    query_params = {
        'serviceKey': _api_decode_key,
        'sigunguCd': sigunguCd,
        'bjdongCd': bjdongCd,
        'bun': bun,
        # 'platGbCd': platGbCd,
        'numOfRows': "100"
    }

    response = requests.get(request_url, params=query_params)
    # print(response.text)
    building_info = format_building_info(response)
    print(f'building_info: {building_info}')


    return 0


if __name__ == '__main__':
    main()
