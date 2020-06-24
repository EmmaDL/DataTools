import unittest

from ProjetFinal import get_links_to_movies, get_html_from_link


def test_get_links_to_movies():
    #Given
    page_link = f'https://www.senscritique.com/films/tops/top111/'
    html = get_html_from_link(page_link)
    
    expected_output = ['/film/12_hommes_en_colere/370894', '/film/Harakiri/402373', '/film/Barberousse/368097', '/film/Le_Bon_la_Brute_et_le_Truand/368376', '/film/Les_Sept_Samourais/451324','/film/Il_etait_une_fois_en_Amerique/804173','/film/Il_etait_une_fois_dans_l_Ouest/440893','/film/Le_Parrain/408443','/film/Le_Trou/440101','/film/Dersou_Ouzala/479434','/film/Point_limite/461381','/film/Entre_le_ciel_et_l_enfer/1324688','/film/Sherlock_Junior/494192','/film/Le_Voyage_de_Chihiro/1367079','/film/L_Aurore/451178','/film/Princesse_Mononoke/376627','/film/Vol_au_dessus_d_un_nid_de_coucou/447958','/film/Pour_Sama/39231333','/film/Pulp_Fiction/445539','/film/Parasite/25357970','/film/Le_Dictateur/478657','/film/Apocalypse_Now/488421','/film/Le_Parrain_2e_Partie/378648','/film/La_Femme_des_sables/409997','/film/Psychose/481802','/film/Voyage_au_bout_de_l_enfer/376439','/film/Quand_passent_les_cigognes/438109','/film/Andrei_Roublev/372818','/film/Les_Affranchis/447001','/film/Boulevard_du_crepuscule/465238','/film/L_Intendant_Sansho/491851','/film/Le_Tombeau_des_lucioles/486492','/film/Requiem_pour_un_massacre/404608','/film/Soy_Cuba/390558','/film/La_Foule/471372','/film/La_vie_est_belle/434210','/film/Rendez_vous/470029','/film/La_Parole/370298','/film/Les_Lumieres_de_la_ville/449464','/film/Jeux_dangereux/465400','/film/Les_Temps_modernes/459866','/film/Les_Enfants_du_paradis/384635','/film/Eve/448394','/film/M_le_maudit/380190','/film/Stalker/719994','/film/Le_Limier/489312','/film/Metropolis/497318','/film/Les_Sentiers_de_la_gloire/415777','/film/Fanny_et_Alexandre/447319','/film/Fight_Club/363185','/film/Le_Kid/365109','/film/Fenetre_sur_cour/407292','/film/La_Nuit_du_chasseur/385235','/film/L_Armee_des_ombres/387436','/film/Un_voyage_avec_Martin_Scorsese_a_travers_le_cinema_americain/452768','/film/Le_Joli_Mai/424606','/film/L_enfer_est_a_lui/424280','/film/Le_13e/22972890','/film/Barry_Lyndon/497324','/film/Memories_of_Murder/453901','/film/Shining/393373','/film/L_Empire_contre_attaque/442615','/film/Persona/402466','/film/La_Verite/364122','/film/La_Colline_des_hommes_perdus/449655','/film/Les_Diaboliques/490354','/film/Autopsie_d_un_meurtre/487417','/film/Les_salauds_dorment_en_paix/493335','/film/Onibaba_les_tueuses/388843','/film/Alien_Le_8eme_Passager/435660','/film/Sueurs_froides/443200','/film/Vivre/462135','/film/Furie/400961','/film/Old_Boy/444625','/film/Le_Seigneur_des_Anneaux_Le_Retour_du_roi/481351','/film/Les_Evades/414626','/film/Chantons_sous_la_pluie/484437','/film/Le_Mecano_de_la_General/365810','/film/Sans_soleil/407618','/film/De_Nuremberg_a_Nuremberg/461726','/film/Paris_Is_Burning/436465','/film/Les_Chaussons_rouges/388384','/film/Faust/428789','/film/La_Bataille_de_Tchernobyl/436363','/film/L_Impasse/492158','/film/Koyaanisqatsi/498132','/film/Une_journee_particuliere/459570','/film/The_Dawn_Wall/37539671','/film/Seven/459080','/film/Whiplash/10777058','/film/La_Liste_de_Schindler/422876','/film/L_Homme_qui_tua_Liberty_Valance/413424','/film/L_Operateur/397809','/film/Elephant_Man/450867','/film/Freaks_La_Monstrueuse_Parade/426746','/film/Citizen_Kane/459226','/film/Paris_Texas/414147','/film/Voyage_a_Tokyo/481639','/film/L_Aventure_de_Mme_Muir/380676','/film/La_Garconniere/423801','/film/Baraka/446509','/film/Mr_Smith_au_Senat/361908','/film/Monty_Python_Sacre_Graal/409839','/film/Le_Salaire_de_la_peur/431892','/film/Ran/369638','/film/La_Passion_de_Jeanne_d_Arc/484119','/film/Nous_nous_sommes_tant_aimes/390103','/film/Le_Gouffre_aux_chimeres/366885','/film/Nous_avons_gagne_ce_soir/418630','/film/Qu_elle_etait_verte_ma_vallee/480998','/film/Orange_mecanique/373525']
    
    #When
    output = get_links_to_movies(html)
    
    #Then
    assert expected_output == output