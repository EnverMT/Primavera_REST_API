from Primavera_REST_Api.__endpointsEnum import EndpointEnum

primaryFields = {
    EndpointEnum.activity: ['Id']
}


requiredFields = {
    EndpointEnum.activity: ['ProjectObjectId', 'WBSObjectId']
}
