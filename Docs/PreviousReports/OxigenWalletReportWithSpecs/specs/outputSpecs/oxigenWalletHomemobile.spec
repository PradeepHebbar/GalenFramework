@objects
	
	    menu   id   menu
	    sess-cash-back   id   sess-cash-back
	    log-user-name   id   log-user-name
	    isUserLogin   id   isUserLogin
	    mobile   id   mobile
	    mb-rec-sub-loader   id   mb-rec-sub-loader
	    form-mobile-recharge   id   form-mobile-recharge
	    mobprepaid   id   mobprepaid
	    monbpostpaid   id   monbpostpaid
	    mobilerecharge-service_number   id   mobilerecharge-service_number
	    mobilerecharge-operator   id   mobilerecharge-operator
	    service_circle   id   service_circle
	    service_operator   id   service_operator
	    service_operator_alias   id   service_operator_alias
	    mobilerecharge-circle   id   mobilerecharge-circle
	    hidden_is_special   id   hidden_is_special
	    mobilerecharge-amount   id   mobilerecharge-amount
	    mb-rechrge-plans   id   mb-rechrge-plans
	    mb_recharge_sub_container   id   mb_recharge_sub_container
	    button-mobile-recharge   id   button-mobile-recharge
	    mb_recharge_conf_container   id   mb_recharge_conf_container
	    button-mobile-confirm-recharge   id   button-mobile-confirm-recharge
	    frm_btn_skip   id   frm_btn_skip
	    landline   id   landline
	    ll-rec-sub-loader   id   ll-rec-sub-loader
	    form-ll-recharge   id   form-ll-recharge
	    landlinerecharge-operator   id   landlinerecharge-operator
	    service_circle   id   service_circle
	    service_operator   id   service_operator
	    service_operator_alias   id   service_operator_alias
	    bsnl-ll-services   id   bsnl-ll-services
	    landlinerecharge-type   id   landlinerecharge-type
	    landlinerecharge-account_number   id   landlinerecharge-account_number
	    show-bsnl-ll-service-no   id   show-bsnl-ll-service-no
	    landlinerecharge-service_number   id   landlinerecharge-service_number
	    landlinerecharge-circle   id   landlinerecharge-circle
	    lopn   id   lopn
	    landlinerecharge-amount   id   landlinerecharge-amount
	    biller_bill_fetch   id   biller_bill_fetch
	    btn_bbfetch   id   btn_bbfetch
	    land-line-recharge-ca-number   id   land-line-recharge-ca-number
	    landlinerecharge-ca_number   id   landlinerecharge-ca_number
	    ll_recharge_sub_container   id   ll_recharge_sub_container
	    button-ll-recharge   id   button-ll-recharge
	    ll_recharge_conf_container   id   ll_recharge_conf_container
	    button-ll-confirm-recharge   id   button-ll-confirm-recharge
	    frm_btn_skip   id   frm_btn_skip
	    dth   id   dth
	    dth-rec-sub-loader   id   dth-rec-sub-loader
	    form-dth-recharge   id   form-dth-recharge
	    dth_steps   id   dth_steps
	    dthrecharge-service_number   id   dthrecharge-service_number
	    dthrecharge-operator   id   dthrecharge-operator
	    service_circle   id   service_circle
	    service_operator   id   service_operator
	    service_operator_alias   id   service_operator_alias
	    dthrecharge-amount   id   dthrecharge-amount
	    dth_recharge_sub_container   id   dth_recharge_sub_container
	    button-dth-recharge   id   button-dth-recharge
	    dth_recharge_conf_container   id   dth_recharge_conf_container
	    button-dth-confirm-recharge   id   button-dth-confirm-recharge
	    frm_btn_skip   id   frm_btn_skip
	    datacard   id   datacard
	    dc-rec-sub-loader   id   dc-rec-sub-loader
	    form-data-card-recharge   id   form-data-card-recharge
	    mobprepaidd   id   mobprepaidd
	    monbpostpaidd   id   monbpostpaidd
	    dc_steps   id   dc_steps
	    datacardrecharge-service_number   id   datacardrecharge-service_number
	    datacardrecharge-operator   id   datacardrecharge-operator
	    service_circle   id   service_circle
	    service_operator   id   service_operator
	    service_operator_alias   id   service_operator_alias
	    datacardrecharge-circle   id   datacardrecharge-circle
	    datacardrecharge-amount   id   datacardrecharge-amount
	    dc_recharge_sub_container   id   dc_recharge_sub_container
	    button-dc-recharge   id   button-dc-recharge
	    dc_recharge_conf_container   id   dc_recharge_conf_container
	    button-dc-confirm-recharge   id   button-dc-confirm-recharge
	    frm_btn_skip   id   frm_btn_skip
	    gas   id   gas
@on [desktop]


=button-mobile-recharge:=
	button-mobile-recharge:
	    width 100% of form-mobile-recharge/width
	    width 335% of mb-rechrge-plans/width
	    width 91% of mb_recharge_sub_container/width
	    width 610% of menu/width
	    width 100% of mobile/width
	    width 174% of mobilerecharge-amount/width
	    width 100% of mobilerecharge-operator/width
	    width 115% of mobilerecharge-service_number/width
	    height 12.6% of form-mobile-recharge/height
	    height 97.4% of mb-rechrge-plans/height
	    height 100% of mb_recharge_sub_container/height
	    height 71.2% of menu/height
	    height 12.6% of mobile/height
	    height 97.4% of mobilerecharge-amount/height
	    height 97.4% of mobilerecharge-operator/height
	    height 97.4% of mobilerecharge-service_number/height
	    inside partly form-mobile-recharge  256px top
	    inside partly mb_recharge_sub_container  15px left, 15px right
	    inside partly mobile  256px top
	    aligned horizontally bottom form-mobile-recharge
	    aligned horizontally all mb_recharge_sub_container
	    aligned horizontally bottom mobile
	    aligned vertically all form-mobile-recharge
	    aligned vertically right mb-rechrge-plans
	    aligned vertically all mobile
	    aligned vertically all mobilerecharge-operator
	    aligned vertically right mobilerecharge-service_number
	    below mb-rechrge-plans 20px
	    below menu 426px
	    below mobilerecharge-amount 20px
	    below mobilerecharge-operator 78px
	    below mobilerecharge-service_number 136px
	    centered horizontally inside mb_recharge_sub_container
=form-mobile-recharge:=
	form-mobile-recharge:
	    width 100% of button-mobile-recharge/width
	    width 335% of mb-rechrge-plans/width
	    width 91% of mb_recharge_sub_container/width
	    width 610% of menu/width
	    width 100% of mobile/width
	    width 174% of mobilerecharge-amount/width
	    width 100% of mobilerecharge-operator/width
	    width 115% of mobilerecharge-service_number/width
	    height 792% of button-mobile-recharge/height
	    height 771% of mb-rechrge-plans/height
	    height 792% of mb_recharge_sub_container/height
	    height 563% of menu/height
	    height 100% of mobile/height
	    height 771% of mobilerecharge-amount/height
	    height 771% of mobilerecharge-operator/height
	    height 771% of mobilerecharge-service_number/height
	    inside partly mobile 
	    aligned horizontally bottom button-mobile-recharge
	    aligned horizontally bottom mb_recharge_sub_container
	    aligned horizontally all mobile
	    aligned vertically all button-mobile-recharge
	    aligned vertically right mb-rechrge-plans
	    aligned vertically all mobile
	    aligned vertically all mobilerecharge-operator
	    aligned vertically right mobilerecharge-service_number
	    below menu 170px
	    centered horizontally inside mb_recharge_sub_container
=mb-rechrge-plans:=
	mb-rechrge-plans:
	    width 29.8% of button-mobile-recharge/width
	    width 29.8% of form-mobile-recharge/width
	    width 27.2% of mb_recharge_sub_container/width
	    width 182% of menu/width
	    width 29.8% of mobile/width
	    width 52% of mobilerecharge-amount/width
	    width 29.8% of mobilerecharge-operator/width
	    width 34.2% of mobilerecharge-service_number/width
	    height 103% of button-mobile-recharge/height
	    height 13% of form-mobile-recharge/height
	    height 103% of mb_recharge_sub_container/height
	    height 73.1% of menu/height
	    height 13% of mobile/height
	    height 100% of mobilerecharge-amount/height
	    height 100% of mobilerecharge-operator/height
	    height 100% of mobilerecharge-service_number/height
	    inside partly form-mobile-recharge  198px top, 214px left, 57px bottom
	    inside partly mobile  198px top, 214px left, 57px bottom
	    aligned horizontally all mobilerecharge-amount
	    aligned vertically right button-mobile-recharge
	    aligned vertically right form-mobile-recharge
	    aligned vertically right mobile
	    aligned vertically right mobilerecharge-operator
	    aligned vertically right mobilerecharge-service_number
	    right-of menu 195px
	    right-of mobilerecharge-amount 0px
	    above button-mobile-recharge 20px
	    above mb_recharge_sub_container 20px
	    below menu 368px
	    below mobilerecharge-operator 20px
	    below mobilerecharge-service_number 78px
=mb_recharge_sub_container:=
	mb_recharge_sub_container:
	    width 110% of button-mobile-recharge/width
	    width 110% of form-mobile-recharge/width
	    width 368% of mb-rechrge-plans/width
	    width 670% of menu/width
	    width 110% of mobile/width
	    width 191% of mobilerecharge-amount/width
	    width 110% of mobilerecharge-operator/width
	    width 126% of mobilerecharge-service_number/width
	    height 100% of button-mobile-recharge/height
	    height 12.6% of form-mobile-recharge/height
	    height 97.4% of mb-rechrge-plans/height
	    height 71.2% of menu/height
	    height 12.6% of mobile/height
	    height 97.4% of mobilerecharge-amount/height
	    height 97.4% of mobilerecharge-operator/height
	    height 97.4% of mobilerecharge-service_number/height
	    aligned horizontally all button-mobile-recharge
	    aligned horizontally bottom form-mobile-recharge
	    aligned horizontally bottom mobile
	    below mb-rechrge-plans 20px
	    below menu 426px
	    below mobilerecharge-amount 20px
	    below mobilerecharge-operator 78px
	    below mobilerecharge-service_number 136px
	    centered horizontally on button-mobile-recharge
	    centered horizontally on form-mobile-recharge
	    centered horizontally on mobile
	    centered horizontally on mobilerecharge-operator
=menu:=
	menu:
	    width 16.4% of button-mobile-recharge/width
	    width 16.4% of form-mobile-recharge/width
	    width 54.9% of mb-rechrge-plans/width
	    width 14.9% of mb_recharge_sub_container/width
	    width 16.4% of mobile/width
	    width 28.6% of mobilerecharge-amount/width
	    width 16.4% of mobilerecharge-operator/width
	    width 18.8% of mobilerecharge-service_number/width
	    height 141% of button-mobile-recharge/height
	    height 17.7% of form-mobile-recharge/height
	    height 137% of mb-rechrge-plans/height
	    height 141% of mb_recharge_sub_container/height
	    height 17.7% of mobile/height
	    height 137% of mobilerecharge-amount/height
	    height 137% of mobilerecharge-operator/height
	    height 137% of mobilerecharge-service_number/height
	    left-of mb-rechrge-plans 195px
	    left-of mobilerecharge-amount 20px
	    left-of mobilerecharge-service_number 20px
	    above button-mobile-recharge 426px
	    above form-mobile-recharge 170px
	    above mb-rechrge-plans 368px
	    above mb_recharge_sub_container 426px
	    above mobile 170px
	    above mobilerecharge-amount 368px
	    above mobilerecharge-operator 310px
	    above mobilerecharge-service_number 252px
=mobile:=
	mobile:
	    width 100% of button-mobile-recharge/width
	    width 100% of form-mobile-recharge/width
	    width 335% of mb-rechrge-plans/width
	    width 91% of mb_recharge_sub_container/width
	    width 610% of menu/width
	    width 174% of mobilerecharge-amount/width
	    width 100% of mobilerecharge-operator/width
	    width 115% of mobilerecharge-service_number/width
	    height 792% of button-mobile-recharge/height
	    height 100% of form-mobile-recharge/height
	    height 771% of mb-rechrge-plans/height
	    height 792% of mb_recharge_sub_container/height
	    height 563% of menu/height
	    height 771% of mobilerecharge-amount/height
	    height 771% of mobilerecharge-operator/height
	    height 771% of mobilerecharge-service_number/height
	    inside partly form-mobile-recharge 
	    aligned horizontally bottom button-mobile-recharge
	    aligned horizontally all form-mobile-recharge
	    aligned horizontally bottom mb_recharge_sub_container
	    aligned vertically all button-mobile-recharge
	    aligned vertically all form-mobile-recharge
	    aligned vertically right mb-rechrge-plans
	    aligned vertically all mobilerecharge-operator
	    aligned vertically right mobilerecharge-service_number
	    below menu 170px
	    centered horizontally inside mb_recharge_sub_container
=mobilerecharge-amount:=
	mobilerecharge-amount:
	    width 57.4% of button-mobile-recharge/width
	    width 57.4% of form-mobile-recharge/width
	    width 192% of mb-rechrge-plans/width
	    width 52.2% of mb_recharge_sub_container/width
	    width 350% of menu/width
	    width 57.4% of mobile/width
	    width 57.4% of mobilerecharge-operator/width
	    width 65.8% of mobilerecharge-service_number/width
	    height 103% of button-mobile-recharge/height
	    height 13% of form-mobile-recharge/height
	    height 100% of mb-rechrge-plans/height
	    height 103% of mb_recharge_sub_container/height
	    height 73.1% of menu/height
	    height 13% of mobile/height
	    height 100% of mobilerecharge-operator/height
	    height 100% of mobilerecharge-service_number/height
	    inside form-mobile-recharge  198px top, 39px left, 91px right, 57px bottom
	    inside mobile  198px top, 39px left, 91px right, 57px bottom
	    inside partly mb-rechrge-plans  91px right
	    aligned horizontally all mb-rechrge-plans
	    aligned vertically left mobilerecharge-service_number
	    left-of mb-rechrge-plans 0px
	    right-of menu 20px
	    above button-mobile-recharge 20px
	    above mb_recharge_sub_container 20px
	    below menu 368px
	    below mobilerecharge-operator 20px
	    below mobilerecharge-service_number 78px
=mobilerecharge-operator:=
	mobilerecharge-operator:
	    width 100% of button-mobile-recharge/width
	    width 100% of form-mobile-recharge/width
	    width 335% of mb-rechrge-plans/width
	    width 91% of mb_recharge_sub_container/width
	    width 610% of menu/width
	    width 100% of mobile/width
	    width 174% of mobilerecharge-amount/width
	    width 115% of mobilerecharge-service_number/width
	    height 103% of button-mobile-recharge/height
	    height 13% of form-mobile-recharge/height
	    height 100% of mb-rechrge-plans/height
	    height 103% of mb_recharge_sub_container/height
	    height 73.1% of menu/height
	    height 13% of mobile/height
	    height 100% of mobilerecharge-amount/height
	    height 100% of mobilerecharge-service_number/height
	    inside partly form-mobile-recharge  140px top, 115px bottom
	    inside partly mobile  140px top, 115px bottom
	    aligned vertically all button-mobile-recharge
	    aligned vertically all form-mobile-recharge
	    aligned vertically right mb-rechrge-plans
	    aligned vertically all mobile
	    aligned vertically right mobilerecharge-service_number
	    above button-mobile-recharge 78px
	    above mb-rechrge-plans 20px
	    above mb_recharge_sub_container 78px
	    above mobilerecharge-amount 20px
	    below menu 310px
	    below mobilerecharge-service_number 20px
	    centered horizontally inside mb_recharge_sub_container
=mobilerecharge-service_number:=
	mobilerecharge-service_number:
	    width 87.2% of button-mobile-recharge/width
	    width 87.2% of form-mobile-recharge/width
	    width 292% of mb-rechrge-plans/width
	    width 79.4% of mb_recharge_sub_container/width
	    width 532% of menu/width
	    width 87.2% of mobile/width
	    width 152% of mobilerecharge-amount/width
	    width 87.2% of mobilerecharge-operator/width
	    height 103% of button-mobile-recharge/height
	    height 13% of form-mobile-recharge/height
	    height 100% of mb-rechrge-plans/height
	    height 103% of mb_recharge_sub_container/height
	    height 73.1% of menu/height
	    height 13% of mobile/height
	    height 100% of mobilerecharge-amount/height
	    height 100% of mobilerecharge-operator/height
	    inside partly form-mobile-recharge  82px top, 39px left, 173px bottom
	    inside partly mobile  82px top, 39px left, 173px bottom
	    aligned vertically right button-mobile-recharge
	    aligned vertically right form-mobile-recharge
	    aligned vertically right mb-rechrge-plans
	    aligned vertically right mobile
	    aligned vertically left mobilerecharge-amount
	    aligned vertically right mobilerecharge-operator
	    right-of menu 20px
	    above button-mobile-recharge 136px
	    above mb-rechrge-plans 78px
	    above mb_recharge_sub_container 136px
	    above mobilerecharge-amount 78px
	    above mobilerecharge-operator 20px
	    below menu 252px
